import requests
from datetime import date


class BitcoinPrice:
    url = ''
    data_from_api = {}
    cached_data = {}
    

    def __init__(self, url):
        self.url = url
        self.data_from_api = self._req_data(url)

    # Получение данных с курсом валют из json файла из api
    def _req_data(self, url):
        try:
            if requests.get(url).status_code == 200:
                response = requests.get(url)
        except:
            raise ConnectionError("Нет доступа к указанному ресурсу")
        return response.json()["bpi"]

    # Получение сырых данных из api
    def raw_data(self):
        return self.data_from_api

    # Расчет стоимости заданного количества битков в заданных валютах
    def btc_calculate(self, bit_count, currency_data=["USD"]):
        self.cached_data = self._bit_convert(bit_count, currency_data)
        return self.cached_data

# разделить на методы

    # Конвертация заданного кол-ва битков в заданные валюты с сохранением в словарь
    def _bit_convert(self, bit_count, currency):
        bit_dict = {}
        for i in self.data_from_api:
            if i in currency:
                bit_dict[i] = {
                                "result" : self._btc_calculate(bit_count, self._get_rate(i)),
                                "btc_count" : bit_count
                                }
        return bit_dict
    
    # Получение текущего курса битка для одной валюты
    def _get_rate(self, currency_counter):
        rate = self.data_from_api[currency_counter]['rate_float']
        return rate
    
    # Функция для получения актуального курса биткоина в заданных валютах
    def get_rate(self, currency):
        rate = [i + ": " + str(self.data_from_api[i]['rate_float']) for i in currency]
        return rate

    # Формула перемножения количества битков на курс с форматирование float с двумя знаками после запятой
    def _btc_calculate(self, bit_count, rate):
        res = bit_count * rate
        print(f'{res = }, {type(res)}')
        return res

    # Форматирование строки с данными конвертации для записи в лог
    def _result(self, bit_count, currency, result):
        output_string = f'[{date.today()}] {bit_count} битков в валюте {currency} = {result}'
        return output_string

    # Вывод в терминал построчно данных из лога
    def print_to_console(self):
        with open("bit_log.txt", "r") as log:
            for i in log:
                print(i)
        # for i in self.cached_data:
        #     print_res = self._result(self.cached_data[i]["btc_count"], i, self.cached_data[i]["result"])
        #     print(print_res)

    # Запись в лог данных построчно из cached.data в формате _result
    def add_to_log(self):
        with open("bit_log.txt", "a") as log:
            for i in self.cached_data:
                log.write(self._result(self.cached_data[i]["btc_count"], i, self.cached_data[i]["result"]) + "\n")
 

if __name__ == '__main__':

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    currency = ("USD", "EUR")

    # Создание экземпляра класса
    req = BitcoinPrice(url)

    # Сырые данные полученные из api
    raw_data = req.raw_data()

    # Курс битка в разных валютах
    rate = req.get_rate(currency)
    # print(f'{rate = }')

    # Расчет и запись в лог конвертации 20 битков в заданных валютах
    bit_count = 20
    calc_data = req.btc_calculate(bit_count, currency)
    req.add_to_log()
    # print(f"{req.data_from_api = }")

    # Расчет и запись в лог конвертации 40 битков в заданных валютах
    bit_count = 40
    calc_data_2 = req.btc_calculate(bit_count,currency)
    req.add_to_log()
    # print(f"{req.data_from_api=}")


# ДЗ 
# Привести класс в порядок 
# Добавить ошибки и исключения 
# Написать тесты к классу ( постараться протестировать все что можно.)
