import random

n = random.randint(3, 20) - 1

result = []

def generate_password(n):
    global result
    for i in range(1, n):
        for j in range(1, n):
            if (j + i) % n == 0:
                result += (i,j)

generate_password(n)

print(f' Выпавшее число: {n}, Пароль: {result}')