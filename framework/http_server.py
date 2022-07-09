# MVC arch model

from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http.cookies import SimpleCookie

import view
import json
import models

# router
# Вызыает Action и передает входящие параметры
# view  - Он и является функцией Action, принимает параметры
# model - Бизнес логика приложения
# render - Каким образом вернуть данные с сервера 
# JOSN, HTML, JSONB, XML


class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""
    # server
    def do_GET(self):
        cookies = SimpleCookie(self.headers.get('Cookie'))
        self.send_response(200)
        self.send_header("Content-type", "application/json")

        if isinstance(dispath(self.path), list):
            action, param = dispath(self.path)
        else:
            raise ValueError(dispath(self.path))

        auth_data = {
            "auth_status": 0,
            "user_login": "",
        }

        if cookies.get("session_id"):
            session_string = cookies['session_id'].value
            login = models.session.Session().check_session(session_string)
            if login:
                auth_data["auth_status"] = 1
                auth_data["user_login"] = login

        if view.func_path.get(action):
            if action == "auth":
                result = view.func_path[action]["action"](param)
                if result["result"]:
                    cookie = SimpleCookie()
                    cookie['session_id'] = models.session.Session().create_session(result["result"])
                    cookie['session_id']['path'] = '/'
                    self.send_header("Set-Cookie", cookie.output(header='', sep=''))
                    result = "User logged in, session active"
                else:
                    result = result["error"]
            else:
                if view.func_path[action]["auth"]:
                    if auth_data.get("auth_status"):
                        result = view.func_path[action]["action"](*param)
                    else:
                        result = "Need authorization"
                else:
                    
                    result = view.func_path[action]["action"](param)
        else:
            result = "Ошибка 404 страница не найдена"

        self.end_headers()

        self.wfile.write(render(result).encode())


def run(server_class=HTTPServer, handler_class=HttpGetHandler):
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()

# dispatcher - path
# https:// - Тип соединения
# habr.com - Домен
# /ru      - Параметр языка
# /post    - Action
# /670872  - Переменная, id поста который нужно отдать


def render(data, error=""):
    result = {
        "result": data,
        "error": error,
    }
    return json.dumps(result)


def dispath(path: str) -> list:
    path_list = path.split('/')
    if len(path_list) < 3:
        print("Wrong input")
    else:
        action = path_list[2]

        if len(path_list) > 3:
            param = path_list[3].split(",")
        else:
            param = []

        return [action, param]

# def check_auth(cookie_value:str)->bool:
