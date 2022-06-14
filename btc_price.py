# Получить внешние данные по ссылке 
# Отдать стоимость btc в нужной валюте 
# Получить стоимость N btc в нужной валюте 
# Вести логирование, и принт по необходимости

from datetime import date
import requests
import pytest

config: dict = {
    "url" : "https://api.coindesk.com/v2/bpi/currentprice.json",
    "log_file" : "bit_log.txt"
} 


def add_to_log_decorator(log_flag=False):
    def logging(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if log_flag == True:
                with open(config['log_file'], "a") as log:
                    log.write(f"[{date.today()}] Function {func.__name__} returned {result}\n")
            return result
        return wrapper
    return logging

class BtcPrice:
    url: str = config["url"]
    btc_price_data: dict = {}
    log_flag: bool = 1


    def __init__(self, url: str = "", log_flag: bool = 0) -> object:
        if url:
            self.url = url
        self.btc_price_data = self._get_data_from_api()
        self.log_flag = log_flag


    
    def _get_data_from_api(self) -> dict:
        try:
            response = requests.get(self.url)
        except:
            raise ConnectionError("Нет доступа к указанному ресурсу Ошибка сервера")
        
        if not response.status_code == 200:
            raise ValueError("HTTP сервер вернул не 200 ответ")

        try:
            resp_data = response.json()
        except:
            raise ValueError("Даннные не json формата")

        if resp_data.get("bpi"):
            return resp_data.get("bpi")
        else:
            raise ValueError("Данные сломаны")

    @add_to_log_decorator(log_flag)
    def get_btc_rate_by_currency(self, currency: str) -> float:
        if not isinstance(currency, str):
            raise TypeError("Валюта должна быть строкой")
        elif not self.btc_price_data.get(currency):
            raise ValueError("Такой валюты не существует")
        rate = self.btc_price_data[currency]["rate_float"]
        if not isinstance(rate, float):
            raise ValueError("Сломанные данные в базе rate_float")
        return rate

    @add_to_log_decorator(log_flag)
    def get_btc_price_by_currency(self, bit_count: int, currency: str) -> float:
        btc_price = bit_count * self.get_btc_rate_by_currency(currency)
        return btc_price


if __name__ == "__main__":

    currency = ("USD", "EUR")
    btc_count = 20
    btc_price_obj = BtcPrice()
    for i in currency:
        print(btc_price_obj.get_btc_rate_by_currency(i))
        print(btc_price_obj.get_btc_price_by_currency(btc_count, i))


def test_init_object():
    fail_code_url = "https://api.coindesk.com/v2/bpi/currensstprice.json"
    fail_request_url = "https://api.coindesk.com2"
    fail_response_data = "https://ya.ru"

    with pytest.raises(ValueError) as e:
        btc_price_obj = BtcPrice(fail_code_url)

    assert "HTTP сервер вернул не 200 ответ" in str(e.value)

    with pytest.raises(ConnectionError):
        btc_price_obj = BtcPrice(fail_request_url)


    with pytest.raises(ValueError):
        btc_price_obj = BtcPrice(fail_response_data)



def test_get_btc_rate():
    btc_price_obj = BtcPrice()
    with pytest.raises(TypeError) as e:
        btc_price_obj.get_btc_rate_by_currency(1)
    assert "Валюта должна быть строкой" in str(e.value)
    with pytest.raises(ValueError) as e:
        btc_price_obj.get_btc_rate_by_currency("RUB")
    assert "Такой валюты не существует" in str(e.value)


def test_get_btc_price():
    btc_price_obj = BtcPrice()
    with pytest.raises(TypeError):
        btc_price_obj.get_btc_price_by_currency("ABR", 3)