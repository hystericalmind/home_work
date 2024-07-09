def uppercase(funk):
    def wrapper():
        original_result = funk()
        modifide_result = original_result.upper()
        return modifide_result
    return wrapper



def great():
    return 'Hello'

great_dec = uppercase(great)



print(great())
print(great_dec())


import time

def time_track(func):
    def surogate(*args, **kwargs):
        started_at = time.time()
        result = func(*args, **kwargs)
        ended_at = time.time()
        elapsed = round(ended_at - started_at, 4)
        print(f'Функция работала: {elapsed} секунды ')
        return result
    return surogate

@time_track
def digist(*args):
    total = 1
    for number in args:
        total *= number ** 5000
    return len(str(total))

result = digist(3141, 5926, 2718, 2818)
print(result)