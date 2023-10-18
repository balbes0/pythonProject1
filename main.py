import random

def main():
    print("Добро пожаловать на Загадочный остров!")
    print("Вы находитесь на берегу острова и перед вами три пути.")
    print("1. Пойти в глубь леса\n2. Пойти к горам\n3. Поплыть на лодке в неизведанные воды")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2/3): "))
        if choice in [1, 2, 3]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        forestgump()
    elif choice == 2:
        mountains()
    elif choice == 3:
        sea()


def forestgump():
    print("Вы отправились в глубь леса.")
    print("1. Пойти к зданию.\n2. Пойти к ручью")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        build()
    elif choice == 2:
        stream()

def build():
    print("Вы пришли к заброшенному зданию.")
    print("Вы видите загадочную дверь с замком.")
    print("Попытаться открыть дверь.\n2. Вернуться обратно в лес")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        if random.random() < 0.5:
            print("Поздравляем! Вы нашли сокровище!")
        else:
            print("К сожалению, дверь закрыта на замок и вы не можете ее открыть.")
    elif choice == 2:
        forestgump()

def stream():
    print("Вы подошли к ручью и заметили мост через него.")
    print("1. Перейти мост.\n2. Вернуться обратно в лес")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Вы успешно перешли мост и продолжили свое приключение.")
        cave()
    elif choice == 2:
        forestgump()

def mountains():
    print("Вы решили отправиться к горам.")
    print("Вы поднимаетесь в горы и видите темную пещеру.")
    print("1. Зайти в пещеру.\n2. Пойти в обход пещеры")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        cave()
    elif choice == 2:
        around_cave()

def cave():
    print("Вы вошли в темную пещеру.")
    print("1. Пойти налево.\n2. Пойти направо")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Вы нашли сокровище! Поздравляем, вы победили игру!")
        exit()
    elif choice == 2:
        print("Вы наткнулись на большого медведя и погибли. Игра окончена.")
        exit()

def around_cave():
    print("Вы решили обойти пещеру.")
    print("1. Взять драгоценный камень.\n2. Продолжить исследование гор")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Поздравляем! Вы нашли драгоценный камень и победили игру.")
        exit()
    elif choice == 2:
        print("Вы продолжаете исследование гор, но больше ничего не находите.")
        exit()

def sea():
    print("Вы решаете поплыть на лодке в неизведанные воды.")
    print("Ваша лодка терпит кораблекрушение на неизведанном острове.")
    print("1. Исследовать остров.\n2. Попытаться починить лодку и вернуться")

    while True:
        choice = int(input("Выберите дальнейшее действие (1/2): "))
        if choice in [1, 2]:
            break
        else:
            print("Введите правильный ответ")

    if choice == 1:
        print("Вы исследуете остров и находите сокровище. Поздравляем, вы победили игру!")
        exit()
    elif choice == 2:
        print("Вы пытаетесь починить лодку, но безуспешно. Игра окончена.")
        exit()

if __name__ == "__main__":
    main()