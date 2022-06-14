from datetime import date

path_dict = {}

def debug_print(log_flag = False):
    print("Функция высшего уровня")

    def actual_decorator(func):
        print(f"Функция  {func.__name__} обернута декоратором debug_print")

        def wrapper(*args):
            print("Функция Третьего уровня")

            print("arguments is", *args)
            result = func(*args)

            if log_flag:
                log_date = f'[{date.today()}] '
                with open("bit_log.txt", "a") as log:
                    log.write(log_date + f"Результат работы функции {result}\n")

            print(f"Результат работы функции {result}")
            return result
        
        return wrapper

    return actual_decorator

def rout(path):
    def actual_decorator(func):
        path_dict[path] = func

        def wrapper(*args):
            print("rout")
            
            return func(*args)

        return wrapper
    return actual_decorator

# @rout("/")
# @debug_print(log_flag=True)
def calculate(value_1, value_2):
    return value_1 * value_2

def decor_func(func):

    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper
 
# "https://api.coindesk.com/v2/bpi/currentprice.json"

if __name__ == "__main__":
    calculate = decor_func(calculate)
    
    # result = dispatcher(url)
    # result = "/"
    # path_dict[result]


# V Декораторы 
# Дописать тесты для Класса нового
# V Для класса написать декораторы логирования
# V Добавить типизацию в класс


"""
    не смог достать логфайл из конфига
    при логировании функция вызванная внутри другой функции повторяет лог (rate)

"""