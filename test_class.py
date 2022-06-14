class Human:
    name = ''
    last_name = ''
    age = int()

    def __init__(self, name, last_name, age):
        self.name = name
        self.last_name = last_name
        self.age = age

    def can_i_buy_beer(self):
        if self.age >= 18:
            return True
        else:
            return False

    def eat(self, food):
        if food == 'apple':
            return f"{self.name} поел {food}"

    def say_name(self):
        print(f"Меня зовут {self.name}")


class Children(Human):

    def say_name(self):
        print(f"Родители не разрешают мне говорить свое имя незнакомцам")

    def eat(self, food):
        super().say_name()
        if food != 'конфета':
            return f"Я не буду есть {food}, я хочу конфету"

fixt_data = {
    1 : {
        "name" : "Александр",
        "last_name" : "Донсков",
        "age" : 33,
    },
    2 : {
        "name" : "Федор",
        "last_name" : "Красинов",
        "age" : 57,
    },
    3 : {
        "name" : "Матвей",
        "last_name" : "Донсков",
        "age" : 5,
    }
}

food = "apple"

for i in fixt_data:
    if fixt_data[i]["age"] > 16:
        human_obj = Human(fixt_data[i]["name"],fixt_data[i]["last_name"],fixt_data[i]["age"])
    else:
        human_obj = Children(fixt_data[i]["name"],fixt_data[i]["last_name"],fixt_data[i]["age"])

    result = human_obj.can_i_buy_beer()
    if result:
        print(f"Человек {human_obj.name} может купить пива")
    else:
        print(f"Человек {human_obj.name} не может купить пива")

    # human_obj.say_name()
    
    print(human_obj.eat(food))