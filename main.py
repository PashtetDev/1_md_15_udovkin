#task1
#print('First commit!')

#19.02.24

#task1
def passCheck():
    pass1 = input("Введите пароль: ")
    pass2 = input("Подтвердите пароль: ")

    if pass1 == pass2:
        print("Пароль принят")
    else:
        print("Пароль не принят")

#task2
def place():
    number = int(input("Введите номер места в вагоне: "))

    str = ""
    if number > 54 or number <= 0:
        str = "Введено недопустимое значение места"
    else:
        str += "Доброе пожаловать в поезд! "

        if number % 2 == 0:
            str += "У вас верхнее место. "
        else:
            str += "У вас нижнее место. "

        if number >= 37:
            str += "У вас боковое место."
        else:
            str += "У вас место в купе"

    print(str)

#task3
def year():
    _year = int(input("Введите год: "))

    if _year < 0:
        print(f"{_year} - не номер года")
        return

    if (_year % 4 == 0 and _year % 100 != 0) or _year % 400 == 0:
        print(f"{_year} - високосный год")
    else:
        print(f"{_year} - не високосный год")

#task4
def colors():
    color1 = input("Введите первый цвет: ")
    color2 = input("Введите второй цвет: ")

    color1 = str.lower(color1)
    color2 = str.lower(color2)

    if not (color1 == "красный" or color1 == "синий" or color1 == "желтый"):
        print("Введен не цвет")
        return

    if not (color2 == "красный" or color2 == "синий" or color2 == "желтый"):
        print("Введен не цвет")
        return

    new_color = color1 + color2

    if "красный" in new_color:
        if "синий" in new_color:
            print("фиолетовый")
        elif "желтый" in new_color:
            print("оранжевый")
        else:
            print("красный")
    elif "синий" in new_color:
        if "желтый" in new_color:
            print("зеленый")
        else:
            print("синий")
    elif "желтый" in new_color:
        print("желтый")

year()