import sys
sys.path.append(r'/home/slava/dev/dev/framework')
from database import DATABASE


if __name__ == '__main__':
    db_obj = DATABASE()
    db_obj.do('''CREATE TABLE IF NOT EXISTS chars
               (
                id int NOT NULL PRIMARY KEY,
                name varchar,
                status varchar,
                species varchar,
                type varchar,
                gender varchar,
                image varchar,
                url varchar,
                created varchar);'''
              )

    db_obj.do('''CREATE TABLE IF NOT EXISTS episodes (
            id int NOT NULL PRIMARY KEY,
            episode TEXT NOT NULL )''')

    db_obj.do('''CREATE TABLE IF NOT EXISTS link (
            id_char int NOT NULL,
            id_episode int NOT NULL )''')
