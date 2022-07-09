import sys
sys.path.append(r'/home/slava/dev/dev/framework')
from database import DATABASE

if __name__ == '__main__':

    db_obj = DATABASE()
    user_list: list = [
        ['vanya', 'sldfkjsd'],
        ['vasya', 'asvouej'],
        ['anna', 'fcceexcv'],
        ['chris', 'jlkj'],
        ['sasha', 'vaihsdd'],
        ['petya', 'asascasc'],
    ]
    for i in user_list:
        db_obj.do("INSERT INTO users values (?, ?)", i)

    data = db_obj.select("SELECT * FROM users")
    for i in data:
        print(i)

