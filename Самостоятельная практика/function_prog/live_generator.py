# Задача 1: Фабрика Функций
# Написать функцию, которая возвращает различные математические функции
# (например, деление, умножение) в зависимости от переданных аргументов.
def gen_1(operation):
    if operation == "add":
        def add(x, y):
            return x + y
        return add
    elif operation == "subtract":
        def subtract(x, y):
            return x - y
        return subtract
    elif operation == 'multiply':
        def multiply(x,y):
            return x * y
        return multiply
    elif operation == 'divide':
        def divide(x, y):
            if y == 0:
                raise ZeroDivisionError
            else:
                return x / y
        return divide


my_func_add = gen_1("add")
my_func_subtract = gen_1('subtract')
my_func_divide = gen_1('divide')
print(my_func_add(2,4))
print(my_func_subtract(4.0, 2.0))
try:
   my_func_divide(10, 0)
except ZeroDivisionError as zero:
    print('Error', 'Division by zero')

# Задача 2: Лямбда-Функции
# Использовать лямбда-функцию для реализации простой операции и написать такую же функцию с использованием def.
# Например, возведение числа в квадрат
print()
print('------------------------------------------------------------------------------------------------------------')
print()

multiply = lambda x, y: x ** y
print(multiply(100, y=2))

def multiply_def(x, y):
   return x ** y
print(multiply_def(100, y=2))


#
# Задача 3: Вызываемые Объекты
# Создать класс с Rect c полями a, b которые задаются в __init__ и методом __call__,
# который возвращает площадь прямоугольника, то есть a*b.

print()
print('------------------------------------------------------------------------------------------------------------')
print()


class Repeater:
   def __init__(self, a, b):
       self.a = a
       self.b =b

   def __call__(self):
       return (f'Стороны : {self.a}, {self.b}  '
               f'\nПлощадь: {self.a * self.b}')

get_area = Repeater(2,4)
print(get_area()) # Выводит [5, 5, 5]