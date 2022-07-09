from database import DATABASE
import time
import random
import string

class Session:
    ttl = 3600

    def create_session(self, login: str) -> str:
        db_obj = DATABASE()
        session_id = self._get_random_string(50)
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
            return ('Invalid session')


    def _get_random_string(self, length: int) -> str:
        # choose from all lowercase letter
        letters = string.ascii_lowercase
        result_str = ''.join(random.choice(letters) for i in range(length))
        # print("Random string of length", length, "is:", result_str)
        return result_str
