import random
#
# n = random.randint(3, 20)
n = 10


result = []

def generate_password(n):
    global result
    for i in range(1, n+1):
        for j in range(1, i):
            if n % (i + j) == 0:
                result +=(i,j)

generate_password(n)

print(f' Выпавшее число: {n}, Пароль: {result[::-1]}')