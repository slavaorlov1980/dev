import model

func_path = {}

def rout(path, auth = 1):

    def actual_decorator(func):
        
        print(f"Находимся в декораторе {func.__name__}")
        func_path[path] = {
            "action" : func,
            "auth" : auth
        }
        
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return actual_decorator

@rout('reg', auth=0)
def reg(log_pass):
    login, password = log_pass.split(',')
    print(login, password)
    model.Auth().register_user(login, password)
    return "User registered"

@rout("auth", auth=0)
def auth(log_pass):
    result = {
        "result" : "",
        "error" : "",
    }  
    if len(log_pass.split(',')) != 2:
        result["error"] = "Wrong login and password"
        return result
    else:
        login, password = log_pass.split(',')
        if model.Auth().check_auth(login, password):
            result["result"] = login

            return result
        else:
            result["error"] = "Incorrect login or password"
            return result

@rout("post")
def post(post_id):
    return f'{post_id}'

@rout("get_btc_rate_by_currency")
def get_btc_rate_by_currency(currency):
    return model.BtcPrice().get_btc_rate_by_currency(currency)

@rout("post_list")
def post_list():
    return "Возвращаем список постов"

@rout("log_out")
def log_out():
    return "Logged out"


# auth - принимает login/pass проверяет валидность.
    # Прописываем пользоватлею куки
# При каждом запросе от пользователя смотрим, есть ли у него куки, и если нет, пишем ему ошибку атворизации
# Если есть, пропускаем дальше. 
# log_out - разлогинивает пользователя
    # Удаляем куки пользователя из браузера
# Если пользователь не авторизован, он не может получить доступ к экшенам

"""
        1. Аутентификация:
    Транспорт    Запрос - /ru/auth/login,passwrd
    Вью - Принимает логин,пароль, трансформирует в удобоваримый вид, и передает дальше.
    Модель - Берем Логин и смотрим если по такому логину, такой пароль. Если - да, то возвращаем True. Если нет такой пары login/pass, то возвращаем false
    Вью - Берет логин и передает в Модель
    Модель - генерирует случайное число(идентификатор) и добавляет пару логин/идентификатор в список активных сессий и задает TTL. Модель возвращает идентификатор-логин.
    Вью - возвращает идентификатор сессии.
    Транспорт - Выставляем куки.( ключевые слова Set Cookie, SimpleCookie, выставить Path = / )
    
        2. Авторизация:
    Транспорт - Получаем куки. 
    Molde - Проверяем активна ли сессия.
    Проверка "Нужна ли авторизация". Если True, проверяем авторизован ли пользователь. Else - сделать действие. 
    Если авторизация нужна и клиент не авторизован, то пошёл в жопу.
"""