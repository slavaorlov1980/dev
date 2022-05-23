import requests


def req_data(url):
    response = requests.get(url)
    return  response.json()

def bit_convert(bit_count, currency, source_data):
    bit_dict = {}
    for i in source_data:
        if i in currency:
            rate = source_data[i]['rate'].replace(',', '')
            bit_dict[i] =  bit_count * float(rate)
    return bit_dict

def print_convert(calc):
    for i in calc:
        print(i, calc[i])

if __name__ == '__main__':
    # Блок данных 
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    bit_count = 20
    currency = ("USD", "EUR")

    # Слой получения данных
    json_data = req_data(url)
    # Слой бизнес логики
    calc_result = bit_convert(bit_count, currency, json_data["bpi"])
    # Слой представления
    print_convert(calc_result)


# Установить
    # done      Linux Ubuntu 20.04 Desktop
    # done      vscode
    # done      live Share
    # done      discord

# Домашнее задание 
    # Задачи по git 
        # done      Зарегистрироваться на github
        # done      Установить git 
        # done      Добавить ssh ключ в github
        # done      Создать публичный репозиторий 
        # done      Сделать первый коммит
        # done      Запушить ветку в репозиторий гитхаб
        #   Создать ветку от мастера 
        #   Сделать коммит 
        #   Запушить ветку в репозиторий гитхам
        #   Сделать pull request 
        #   Добавить меня к коллаборации репозитория (Ник BanaKing)
    # Документация docstring функций
    # Unit tests 
    # Классы модули в python
    # Декораторы