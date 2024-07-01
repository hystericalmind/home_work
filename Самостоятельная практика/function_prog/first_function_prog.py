list_0 = [1, 2, 5, 7, 12, 11, 35, 4, 89, 10]

def serch_vallue(args):
    return args % 2

def degree(args):
    return args ** 2

result_0 = map(degree,filter(serch_vallue, list_0))
print(list(result_0))
