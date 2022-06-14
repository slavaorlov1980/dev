import model

func_path = {}

def rout(path):

    def actual_decorator(func):
        
        print(f"Находимся в декораторе {func.__name__}")
        func_path[path] = func
        
        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return actual_decorator

@rout("auth")
def auth(log_pass):
    if len(log_pass.split(',')) != 2:
        return "Wrong login and password"
    else:
        login, password = log_pass.split(',')
        if login == "vasya" and password == "1234":
            return "Login is correct"
        else:
            return "Incorrect Login or password"

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