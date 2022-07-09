import json
import sqlite3


class RickMortyDB:
    url: str = 'rnm_char_data.json'
    db_name = 'rick_and_morty.db'
    con: str = ''
    cur: str = ''

    def _connect(self):
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()

    def _close_conect(self):
        if self.con:
            self.con.close()

    def do(self, query: str, param: list = []) -> bool:
        self._connect()
        self.cur.execute(query, param)
        self.con.commit()
        self._close_conect()
        return True

    def select(self, query: str, param: list = []) -> list:
        self._connect()
        data: list = list()

        for i in self.cur.execute(query, param):
            data.append(i)

        self._close_conect()

        return data


if __name__ == '__main__':
    obj = RickMortyDB()
    obj.do('''CREATE TABLE IF NOT EXISTS characters
           (
            id int NOT NULL,
            name varchar,
            status varchar,
            species varchar,
            type varchar,
            gender varchar,
            image varchar,
            url varchar,
            created varchar,
            PRIMARY KEY (id) );'''
           )

#    obj.do("INSERT INTO characters VALUES (1, 'Rick', 'alive', 'human', 'none', 'male', 'http://img', 'http://url', '2008-11-11 13:23:44');")

    data = obj.select("SELECT name, status FROM characters;")
    for i in data:
        print(i)

'''
    0. Создаем таблицы множественных значений (эпизоды, происхождение etc)
    1. Цикл по списку словарей
    2. Если длина значения ключа = 1, то инсерт в основную таблицу в колонку ключ значения, если праймари ки = id (или через создание списка значений)
    3. Else если длина значения больше одного, создаем таблицу связей для праймари ки и таблицы значений с именем ключа
'''
