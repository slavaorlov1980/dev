import sys
sys.path.append(r'/home/slava/dev/dev/framework')
from database import DATABASE



if __name__ == '__main__':
    db_obj = DATABASE()
    db_obj.do('''CREATE TABLE IF NOT EXISTS session (
            date timestamp,
            login TEXT NOT NULL,
            session_id TEXT NOT NULL )''')
    db_obj.do('''CREATE TABLE users (
            login TEXT NOT NULL PRIMARY KEY,
            password TEXT NOT NULL )''')


# print(db_obj.select("SELECT * FROM sqlite_schema WHERE type ='table' AND name NOT LIKE 'sqlite_%'"))
