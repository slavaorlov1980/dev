import requests 


config: dict = {
    "url" : "https://api.coindesk.com/v2/bpi/currentprice.json",
} 

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

    def get_btc_rate_by_currency(self, currency: str) -> float:
        if not isinstance(currency, str):
            raise TypeError("Валюта должна быть строкой")
        elif not self.btc_price_data.get(currency):
            raise ValueError("Такой валюты не существует")
        rate = self.btc_price_data[currency]["rate_float"]
        if not isinstance(rate, float):
            raise ValueError("Сломанные данные в базе rate_float")
        return rate

    def get_btc_price_by_currency(self, bit_count: int, currency: str) -> float:
        btc_price = bit_count * self.get_btc_rate_by_currency(currency)
        return btc_price