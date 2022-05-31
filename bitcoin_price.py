import requests
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
        return response.json()["bpi"]


    def raw_data(self):
        return self.data_from_api


    def btc_calculate(self, bit_count, currency_data=["USD"]):
        self.cached_data = self._bit_convert(bit_count, currency_data)
        return self.cached_data

# разделить на методы

    def _bit_convert(self, bit_count, currency):
        bit_dict = {}
        for i in self.data_from_api:
            if i in currency:
                bit_dict[i] = {
                                "result" : self._btc_calculate(bit_count, self._get_rate(i)),
                                "btc_count" : bit_count
                                }
        return bit_dict
    

    def _get_rate(self, currency_counter):
        rate = self.data_from_api[currency_counter]['rate'].replace(',', '')
        return float(rate)


    def _btc_calculate(self, bit_count, rate ):
        return f"{(bit_count * rate):,.2f}"


    def _result(self, bit_count, currency, result):
        output_string = f'[{date.today()}] {bit_count} битков в валюте {currency} = {result}'
        return output_string


    def print_to_console(self):
        with open("bit_log.txt", "r") as log:
            for i in log:
                print(i)
        # for i in self.cached_data:
        #     print_res = self._result(self.cached_data[i]["btc_count"], i, self.cached_data[i]["result"])
        #     print(print_res)


    def add_to_log(self):
        with open("bit_log.txt", "a") as log:
            for i in self.cached_data:
                log.write(self._result(self.cached_data[i]["btc_count"], i, self.cached_data[i]["result"]) + "\n")
 

if __name__ == '__main__':

    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    bit_count = 20
    currency = ("USD", "EUR")

    req = BitcoinPrice(url)

    # Сырые данные полученные из api 
    raw_data = req.raw_data()
    calc_data = req.btc_calculate(bit_count, currency)
    req.add_to_log()

    bit_count = 40
    calc_data_2 = req.btc_calculate(bit_count,currency)
    req.add_to_log()

    req.print_to_console()

    print(f"{calc_data = }")
    print(f"{calc_data_2 = }")


# ДЗ 
# Привести класс в порядок 
# Добавить ошибки и исключения 
# Написать тесты к классу ( постараться протестировать все что можно.)
