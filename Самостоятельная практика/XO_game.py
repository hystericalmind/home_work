

def draw_area():

    for i in area:
        print(*i)
    print()

area = [['*', '*', '*'], ['*', '*', '*'], ['*', '*', '*'], ]
print("Добро пожаловато в крестики-нолики")
print("------------------------------------")
for step in range(1,10):
    print(f'Ход: {step}')
    if step % 2 == 0:
        step_char = 'O'
        print('Ходят нолики')
    else:
        step_char = 'X'
        print('Ходят крестики')
    draw_area()
    row = int(input('Введите номер строки (1,2,3) :')) - 1
    column = int(input('Ведите номер столбца (1,2,3) :')) - 1
    if area[row][column] == '*':
        area[row][column] = step_char
        # insert_enter = int(input())
    # elif insert_enter != ('X' or 'O'):
    #     print("символ не введен, переход хода")


    else:
        print('ячейка уже занята, переход хода')
        draw_area()
        continue

def check_winner():
    if area[0][0] == 'X' and area[0][1] == 'X' and area[0][2] == 'X':
        return 'X'
    if area[1][0] == 'X' and area[1][1] == 'X' and area[1][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[2][1] == 'X' and area[2][2] == 'X':
        return 'X'

    if area[0][0] == 'O' and area[0][1] == 'O' and area[0][2] == 'O':
        return 'O'
    if area[1][0] == 'O' and area[1][1] == 'O' and area[1][2] == 'O':
        return 'O'
    if area[2][0] == 'O' and area[2][1] == 'O' and area[2][2] == 'O':
        return 'O'

    if area[0][0] == 'X' and area[1][0] == 'X' and area[2][O] == 'X':
        return 'X'
    if area[0][1] == 'X' and area[1][1] == 'X' and area[2][1] == 'X':
        return 'X'
    if area[0][2] == 'X' and area[1][2] == 'X' and area[2][2] == 'X':
        return 'X'

    if area[0][0] == 'O' and area[1][0] == 'O' and area[2][O] == 'O':
        return 'O'
    if area[0][1] == 'O' and area[1][1] == 'O' and area[2][1] == 'O':
        return 'O'
    if area[0][2] == 'O' and area[1][2] == 'O' and area[2][2] == 'O':
        return 'O'

    if area[0][0] == 'X' and area[1][1] == 'X' and area[2][2] == 'X':
        return 'X'
    if area[2][0] == 'X' and area[1][1] == 'X' and area[0][2] == 'X':
        return 'X'

    if area[0][0] == 'O' and area[1][1] == 'O' and area[2][2] == 'O':
        return 'O'
    if area[2][0] == 'O' and area[1][1] == 'O' and area[0][2] == 'O':
        return 'O'
    return '*'

draw_area()

if check_winner() == 'X':
    print('TODAY WIN X PLAYER')

if check_winner() == 'O':
    print('TODAY WIN O PLAYER')

if check_winner() == '*' and step_char == 9:
    print('TODAY WIN O PLAYER')












