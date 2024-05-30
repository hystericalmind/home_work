data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = (data_structure)


def data_sort(*data_structure):
    list_0 = 0
    dict_0 = {}
    dict_1 = {}
    tuple_0 = 0
    for i in data_structure:
        for j in i:
            if isinstance(j, list):
                list_0 = sum(j)
                print('Это сумма списка:', list_0)

            elif isinstance(j, dict):
                dict_0 = (len(j) + (sum(j.values())))
                print('Это сумма словаря:', dict_0)

            def data_sum():

                if isinstance(j, tuple):
                    for k in j:
                        print('Это содержимое  кортежа :', k)
                        if isinstance(k, tuple):
                            tuple_0 = int(sum(k))
                            print('это если в кей есть кортеж:', tuple_0)
                        elif isinstance(k, dict):
                            dict_1 = (len(k) + (sum(k.values())))
                            print('это если в кей есть словарь:', dict_1)
                # print('это сумма кортежей:', sum(zip(k)))

                # if isinstance(k,dict):
                #     dict_1 = (len(k) + (sum(k.values())))
                #     print(k)
                #     print(sum(k.values()))
                #     print(dict_1)
            data_sum()





data_sort(data_structure)


print()

print()

print()



