import random

def f():

    qest = {1:"Котангенс 135 градусов?", 2:"Сколько хромосом у человека?", 3:"Сколько аксиом в стереометрии?", 4:"Сколько дней в обычном году?", 5:"Сколько спиралей в молекуле ДНК?"}
    list = [1, 2, 3, 4, 5]

    for i in range(5):
        num = random.choices(list)
        num = str(num)
        num = num.replace('[', '')
        num = num.replace(']', '')
        num = int(num)
        list.remove(num)
        ans = input(qest[num])
        if num == 1:
            while ans != '-1':
                print("Ответ не верен, поробуйте ещё раз!")
            else:
                print("Ответ верен, продолжим!")
        if num == 2:
            while ans != '46':
                print("Ответ не верен, поробуйте ещё раз!")
            else:
                print("Ответ верен, продолжим!")
        if num == 3:
            while ans != '3':
                print("Ответ не верен, поробуйте ещё раз!")
            else:
                print("Ответ верен, продолжим!")
        if num == 4:
            while ans != '365':
                print("Ответ не верен, поробуйте ещё раз!")
            else:
                print("Ответ верен, продолжим!")
        if num == 5:
            while ans != '4':
                print("Ответ не верен, поробуйте ещё раз!")
            else:
                print("Ответ верен, продолжим!")

    print("Поздравляю вы прошли викторину!")
    l = input("Сыграть ещё раз?(Да, Нет)")
    if l == "Да":
        f()


