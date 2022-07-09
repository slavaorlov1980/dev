from database import DATABASE
import sqlite3

class Users:

    def __init__(self, login: str):
        db_obj = DATABASE()
        data = db_obj.select("SELECT login, password  FROM users WHERE login = ?", [login])

        if data:
            self.password = data[-1][1]
            self.login = data[-1][0]
        else:
            raise ValueError("User doesn't exist")

    @staticmethod
    def create_user(login: str, password: str) -> object:
        db_obj = DATABASE()
        try:
            db_obj.do("INSERT INTO users values (?, ?)", [login, password])
            return Users(login)
        except sqlite3.Error as e:
            print('registration error:', e.args[0])
        
