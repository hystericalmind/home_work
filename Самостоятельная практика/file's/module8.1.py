

def add_everything_up(a, b):
    return (f'{a},{b}')


a = (int or float)
b = str


try:
    a == str

except(TypeError):
    print("input data - type error(non int or float)")
try:
    b == (int or float)
except(TypeError):
    print("input data - type error(non str)")
finally:
    pass

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
