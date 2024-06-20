

def add_everything_up(a, b):
    # result = a + b
    return (f'{a},{b}')


a = (int or float)
b = str


try:
    a != int and a != float
except(TypeError):
    print("input data - type error(non int or float)")
try:
    b != str
except(TypeError):
    print("input data - type error(non str)")


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))

