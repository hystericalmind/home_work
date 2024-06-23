class InvalidDataException(Exception):
    def __init__(self, massage, class_info):
        self.massage = massage
        self.class_info = class_info

class ProcessingException(Exception):
    def __init__(self, massage, class_info):
        self.massage = massage
        self.class_info = class_info


def exc_generat_1(a, b):
    result = b + a
    if b == 0:
        raise InvalidDataException('Не правильный параметр','Параметр должен быть больше 0')
    return result

def big_problem(c, d):
    total = c * d
    if d > 150:
        raise ProcessingException("Найдена ошибка в процессах",
                                  'первый параметр не может быть больше 150')
    return total

try:
    result_1 = exc_generat_1(200,0)
    print(result_1)
except InvalidDataException as inv:
    print(f'Была обнаружена ошибка  "{inv.massage}". Чтобы все заработало: {inv.class_info}"')
try:
    result_2 = big_problem(20, 400)
except ProcessingException as proc:
    print(f'Была обнаружена СОВСЕМ ДРУГАЯ ОШИБКА, {proc.massage}, решение простое: {proc.class_info} ')

