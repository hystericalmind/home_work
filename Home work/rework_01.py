import random


def print_params(param):
    list_0 = list(range(2, 20))
    for i in list_0:
        args_1 = random.choice(list_0)
        list_0.remove(args_1)
        args_2 = random.choice(list_0)
        list_0.remove(args_2)

        print(
            f'Было выбрано сдучайное число : {args_1}. Был ввенден аргумен: {param}. Был умножен параметр на элемент списка {args_1 * param}')
        print(
            f'Было: выбрано случайное число : {args_2}. Был ввенден аргумен: {param}. Был умножен параметр на элемент списка: {args_2 * param}')


        break

print_params(300)