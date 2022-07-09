import requests
import random
import string
import time
import os
from database import DATABASE


config: dict = {
    "url": "https://api.coindesk.com/v2/bpi/currentprice.json",
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


class Users:

    def __init__(self, login: str):
        db_obj = DATABASE()
        data = db_obj.select("SELECT login, password  FROM users WHERE login = ?", [login])
        # print("user_init")
        # print(data)
        if data:
            self.password = data[-1][1]
            self.login = data[-1][0]
        else:
            raise ValueError("User doesn't exist")

    @staticmethod
    def create_user(login: str, password: str) -> object:
        db_obj = DATABASE()
        db_obj.do("INSERT INTO users values (?, ?)", [login, password])
        return Users(login)



class Auth:

    def register_user(self, login: str, password: str) -> bool:

        Users.create_user(login, password)
        return True

    def check_auth(self, login: str, password: str) -> bool:
        try:
            user = Users(login)
            print(user)

        except ValueError:
            print("checkout")

            return False
        print("checkout")
        print(user.login, user.password, password)
        if password == user.password:
            return True

        return False


class Session:
    ttl = 3600

    def create_session(self, login: str) -> str:
        db_obj = DATABASE()
        session_id = self.get_random_string(50)
        create_date = int(time.time())
        
        result = db_obj.do('INSERT INTO session VALUES (?, ?, ?)', [create_date, login, session_id])
        if result:
            return session_id

    # Понимание, что TTL закончился, должно работать на уровне SQL запроса
    def check_session(self, session_id: str) -> str:
        db_obj = DATABASE()
        time_now = int(time.time())
        login = db_obj.select('SELECT login FROM session WHERE session_id = ? AND (? - date < ?)', [session_id, time_now, self.ttl])
        if login:
            return login
        else:
            raise ValueError('Session not found in DB')

    def get_random_string(self, length: int) -> str:
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        # print("Random string of length", length, "is:", result_str)
        return result_str
