import requests
import btc_calculate
from datetime import date

class BitcoinPrice:
    url = ''
    data_from_api = {}
    cached_data = {}
    
    def __init__(self, url):
        self.url = url
        self.data_from_api = self._req_data()

    def _req_data(self):
        response = requests.get(self.url)
        return  response.json()

    def raw_data(self):
        return self.data_from_api

    def btc_calculate(self, bit_count, currency_data=["USD"]):
        self.cached_data = self.bit_convert(bit_count, currency_data)

        return self.cached_data

    def bit_convert(self, bit_count, currency):
        bit_dict = {}
        for i in self.data_from_api:
            if i in currency:
                rate = self.data_from_api[i]['rate'].replace(',', '')
                bit_dict[i] =  {
                    "result" : self._btc_calculate(bit_count, float(rate)),
                    "btc_count" : bit_count,
                }
                print(bit_dict[i])
        return bit_dict
    
    def _btc_calculate(self, bit_count, rate ):
        return bit_count * rate

    def _result(self, bit_count, currency, result):
        print_res = f'[{date.today()}] {bit_count} битков в валюте {currency} = {result}'


    def print_to_console(self):
        for i in self.cached_data:
            print_res = self._result(self.cached_data[i]["btc_count"], i, self.cached_data[i]["result"])
            print(print_res)

    # def print_convert(calc, bit_count):
    #     for i in calc:
            
    #         print_res = f'[{date.today()}] {bit_count} битков в валюте {i} = {calc[i]}'
    #         print(print_res)
    #         bit_log = open('bit_log.txt', 'a')
    #         bit_log.write(print_res + '\n')
    #         bit_log.close()


if __name__ == '__main__':
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    bit_count = 20
    currency = ("USD", "EUR")

    req = BitcoinPrice(url)
    # Сырые данные полученные из api 
    raw_data = req.raw_data()
    calc_data = req.btc_calculate(bit_count, currency)
    bit_count = 40
    calc_data_2 = req.btc_calculate(bit_count,currency)

    # req.save_to_log()
    req.print_to_console()

    # Блок данных 
    # print(req.data_from_api)
    # # Слой получения данных
    # json_data = req.req_data(url)
    # # Слой бизнес логики
    # calc_result = req.bit_convert(bit_count, currency, json_data["bpi"])
    # # Слой представления
    # req.print_convert(calc_result, bit_count)


# ДЗ 
# Привести класс в порядок 
# Добавить ошибки и исключения 
# Написать тесты к классу ( постараться протестировать все что можно.)
