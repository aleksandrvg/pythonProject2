import math


def square():
    choice = input('Выберите фигуру: 1 - прямоугольник, 2 - круг, 3 - трапеция, 4 - треугольник: ')
    if choice == '1':
        a = int(input('Введите сторону a: '))
        b = int(input('Введите сторону b: '))
        print(f'Площадь прямоугольника: {a * b}')
    elif choice == '2':
        r = int(input('Введите радиус: '))
        print(f'Площадь круга: {math.pi * r ** 2}')
    elif choice == '3':
        a = int(input('Введите сторону a: '))
        b = int(input('Введите сторону b: '))
        h = int(input('Введите высоту: '))
        print(f'Площадь трапеции: {((a + b) * h) / 2}')
    elif choice == '4':
        a = int(input('Введите сторону a: '))
        b = int(input('Введите сторону b: '))
        print(f'Площадь треугольника: {(a * b) / 2}')
    else:
        print('Ввод не верный. Выберите фигуру.')


def perimeter():
    choice = input('Выберите фигуру: 1 - прямоугольник, 2 - круг, 3 - трапеция: ')
    if choice == '1':
        a = int(input('Введите сторону a: '))
        b = int(input('Введите сторону b: '))
        print(f'Периметр прямоугольника: {a + a + b + b}')
    elif choice == '2':
        r = int(input('Введите радиус: '))
        print(f'Периметр круга: {2 * math.pi * r}')
    elif choice == '3':
        a = int(input('Введите сторону a: '))
        b = int(input('Введите сторону b: '))
        c = int(input('Введите сторону c: '))
        d = int(input('Введите сторону d: '))
        print(f'Периметр трапеции: {a + b + c + d}')
    else:
        print('Ввод не верный. Выберите фигуру.')


def figure():
    while True:
        print('Программа для рассчета (для выхода введите: exit)')
        choice = input('Выберите что нужно рассчитать: 1 - площадь фигуры, 2 - периметр фигуры: ')
        if choice == '1':
            square()
        elif choice == '2':
            perimeter()
        else:
            print('Ввод не верный. Выберите фигуру.')
        if choice == 'exit':
            break


figure()
