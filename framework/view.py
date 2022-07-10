import models
func_path = {}


def rout(path, auth=1):

    def actual_decorator(func):

        print(f"Находимся в декораторе {func.__name__}")
        func_path[path] = {
            "action": func,
            "auth": auth
        }

        def wrapper(*args, **kwargs):
            return func(*args, **kwargs)
        return wrapper

    return actual_decorator


@rout('reg', auth=0)
def reg(login, password):
    # login, password = log_pass
    if models.auth.Auth().register_user(login, password):
        models.session.Session().create_session(login)
        return "User registered"
    else:
        return "Login already exists"


@rout("auth", auth=0)
def auth(login, password):
    result = {
        "result": "",
        "error": "",
    }
    if not login or not password:
        result["error"] = "Wrong login and password"
        return result
    else:
        # login, password = log_pass
        if models.auth.Auth().check_auth(login, password):
            result["result"] = login
            return result
        else:
            result["error"] = "Incorrect login or password"
            return result


@rout("get_user_data")
def get_user_data(login):
    user = models.users.Users(login)
    return (user.login, user.password)


@rout("post")
def post(post_id):
    return f'{post_id}'


@rout("get_btc_rate_by_currency")
def get_btc_rate_by_currency(currency):
    return models.btc_price.BtcPrice().get_btc_rate_by_currency(currency)


@rout("post_list")
def post_list():
    return "Возвращаем список постов"


@rout("most_popular")
def most_popular():
    name = models.rick_and_morty.CharList().most_popular_char()
    return name


@rout("most_popular_dead")
def most_popular_dead():
    name = models.rick_and_morty.CharList().most_popular_dead()
    return name

@rout("all_chars_episode")
def all_chars_episode(ep):
    char_list = models.rick_and_morty.CharList().all_chars_in_episode(ep)
    return char_list


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
