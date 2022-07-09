import sqlite3


class DATABASE:
    db_name = '/home/slava/dev/dev/framework/database.db'
    con = ''
    cur = ''

    def _connect(self):
        self.con = sqlite3.connect(self.db_name)
        self.cur = self.con.cursor()

    def _close_connect(self):
        if self.con:
            self.con.close()

    def do(self, query: str, param: list = []) -> bool:
        self._connect()
        self.cur.execute(query, param)
        self.con.commit()
        self._close_connect()
        return True

    def select(self, query: str, param: list = []) -> list:
        self._connect()
        data: list = list()

        for i in self.cur.execute(query, param):
            data.append(i)

        self._close_connect()

        return data


if __name__ == '__main__':
    db_obj = DATABASE()
    db_obj.do('''CREATE TABLE IF NOT EXISTS session (
        date timestamp,
        login TEXT NOT NULL,
        session_id TEXT NOT NULL )'''
     )

    # db_obj.do("INSERT INTO session VALUES (?, ?, ?)",
    #           (1655857859, 'vanylaskdfjdlka',
    #            'kjxcujrmaqzbnsphbbhkinljtdysroomapahkforqovcxwjrds'))

    data = db_obj.select("SELECT * FROM session WHERE login = ?", ["vanya"])
    print(type(data))
    for i in data:
        print(i)
