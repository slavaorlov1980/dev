from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
from http.cookies import SimpleCookie

import view
import json
# Set-Cookie: <cookie-name>=<cookie-value>

# router
# Вызыае ACtion и передает входящие параметры
# view  - Он и является функцией Action, принимает параметры
# model - Бизнес логика приложения
# render - Каким образом вернуть данные с сервера 
# JOSN, HTML, JSONB, XML

class HttpGetHandler(BaseHTTPRequestHandler):
    """Обработчик с реализованным методом do_GET."""
# server 
    def do_GET(self):
        cookies = SimpleCookie(self.headers.get('Cookie'))
        print('headers =', self.headers)
        auth_state = 0
        if isinstance(dispath(self.path), list):
            action, param = dispath(self.path)
        else:
            raise ValueError("Chozanax")

        cookie = SimpleCookie()
        cookie['user_id'] = '1234'
        cookie['user_id']['path'] = '/'
        
        self.send_response(200)
        self.send_header("Content-type", "application/json")

        if view.func_path.get(action):
            if action == "auth":
                result = view.func_path[action](param)
                if result == "Login is correct":
                    self.send_header("Set-Cookie", cookie.output(header='',sep=''))
            elif cookies:
                auth_state = check_auth(cookies['user_id'].value)
                if auth_state:
                    if action == "log_out":
                        if "user_id" in cookies:
                            cookie['user_id']['expires'] = "Sun, 06 Nov 1994 08:49:37 GMT"
                            self.send_header("Set-Cookie", cookie.output(header='',sep=''))
                            result = view.func_path[action]()
                    else:
                        result = view.func_path[action](param)
                else:
                    result = "Ошибка авторизации"
            else:
                result = "Access denied for unregistered users"
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

def render(data, error = ""):
    result =  {
        "result" : data,
        "error" : error,
    }
    return json.dumps(result)

def dispath(path:str)->list:
    path_list = path.split('/')
    if len(path_list) != 4:
        return "Wrong input"
    else:
        action = path_list[2]
        param = path_list[3]
        return [action, param]

def check_auth(cookie_value:str)->bool:
    if cookie_value == '1234':
        return True
    else:
        return False