import requests 
import random
import string
import time


config: dict = {
    "url" : "https://api.coindesk.com/v2/bpi/currentprice.json",
    "login_db" : {'vasya' : '1234',
                  'slava' : '123',
                  'valery' : '321',
                  }
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

class Auth:
    user_data:str = "user.data"

    def register_user(self, login:str, password:str) -> bool:
        with open(self.user_data, "r") as file:
            data_base = file.read().split(',')

        with open(self.user_data, "a") as file:
            for i in data_base:
                if login == i.split(':')[0]:
                    return False
                else:
                    file.write(f'{login}:{password},')
                    return True


    def check_auth(self, login:str, password:str) -> bool:
        with open(self.user_data, 'r') as file:
            data_base = file.read().split(',')
            for i in data_base:
                log, psw = i.split(':')
                if login == log and password == psw:
                    return True
        return False

class Session:
    session_data:str = 'session.data'
    ttl = 3600

    def create_session(self, login:str)->str:
        with open(self.session_data, 'a') as file:
            session_id = self.get_random_string(50)
            create_date  = int(time.time())
            result = f'{create_date}:{login}:{session_id},'
            file.write(result)
        return result

    def check_session(self, session_id:str)->str:
        with open(self.session_data, 'r') as file:
            session_data = file.read().split(',')
            for i in session_data:
                date, login, id = i.split(':')
                time_now = int(time.time())
                if session_id == id and time_now-date > self.ttl:
                    return login
        

    def get_random_string(self, length:int)->str:
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        # print("Random string of length", length, "is:", result_str)
        return result_str



# Имя класса:
# Какие даныне этот класс представляет
    # Есть файл user.data в котом лежат данные в виде
    # login:passwd,login_2:passwd_2,
# Общее описание класса 
# Методы классаа
# регистрация пользователя(вносит даные в файл user.data, принимает логин, пароль, возвращает обновленный файл)
# проверка логина и пароля на наличие в базе (проверяет, зареган ли юзер. принимает логин, пароль. возвращает буль)

#     Что делает метод
#     Какие данные ему нужны для БЛ
#     Какие данные он возвращает 

