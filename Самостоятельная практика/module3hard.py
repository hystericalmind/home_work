data_structure = [[1, 2, 3],
                  {'a': 4, 'b': 5},
                  (6,{'cube': 7, 'drum': 8}),
                  "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = (data_structure)


def data_sort(*data_structure):
    list_0 = 0
    list_1 = []
    dict_0 = {}
    dict_1 = {}
    dict_2 = {}
    dict_3 =[]
    tuple_0 = 0
    tuple_1 = []
    def iterator(*args):

        for i in data_structure:

            for j in i:

                if isinstance(j, list):
                    list_0 = sum(j)
                    print('Это сумма списка:', list_0)
                if isinstance(j, dict):
                    dict_0 = (len(j) + (sum(j.values())))
                    print('Это сумма  первого словаря:', dict_0)

                if isinstance(j, tuple):
                    print('JJJJJJJ',j)
                    for k in j:
                        if isinstance(k, dict):
                            dict_0 = (len(k) + (sum(k.values())))
                            print('Это сумма  вложенного словаря:', dict_0)
                        if isinstance(k, int):
                            print("ЭТО ЦИФРА", k )
                    for recursion in j:
                        if isinstance(recursion, list):
                            print(len(recursion))
                        if isinstance(recursion, dict):
                            if isinstance(recursion, tuple):
                                iterator(recursion)

                                print('eeeeeeee')
                        if isinstance(j, str):
                            print('aaaaaaaaaeeeeee',len(j))




                # def recursion():
                #     if isinstance(i, list):
                #
                # recursion()

    iterator()
data_sort(data_structure)

#
# def dict_detect(*args):
#     if  isinstance(args, dict):
#         for i in args:
#             dict_0 = (len(i) + (sum(i.values())))
#             print('Это сумма словаря:', dict_0)


            # if isinstance(j, list):
            #     list_0 = sum(j)
            #     print('Это сумма списка:', list_0)
            #
            # if isinstance(j, dict):
            #     dict_0 = (len(j) + (sum(j.values())))
            #     print('Это сумма словаря:', dict_0)
            #
            # if isinstance(j, str):
            #     print("Это содержимое в БУКОВКАХ:", j)
            #
            # if isinstance(j, tuple):
            #     for k in j:
            #         if isinstance(k, int):
            #             print('ПЕРВАЯ ЦИФРА', k)
            #         if isinstance(k, dict):
            #             dict_1 = (len(k) + (sum(k.values())))
            #             print('Это сумма словаря 2222222222222222:', dict_1)
            #         if isinstance(k, list):
            #             list_1 = k
            #             print('Это сумма списка 33333333333333333:', list_1)
            #
            #             print('Это содержимое  кортежа :', k)
            #         print(type(k))
            #         if isinstance(k, list):
            #             list_0 += sum(k)
            #             print('Это сумма списка:', list_0)
            #
            #         if isinstance(k, dict):
            #             dict_0 = (len(k) + (sum(k.values())))
            #             print('Это сумма словаря:', dict_0)
            #






#
#     def data_sum():
#
#         if isinstance(j, tuple):
#             for k in j:
#                 print('Это содержимое  кортежа :', k)
#                 if isinstance(k, tuple):
#                     tuple_1 = k
#                     print(k)
#                     if isinstance(k, dict):
#                         dict_3 = k
#                         print('pdddddt,bmc', dict_3)
#                     data_sum()
#                     #             for recurs_1 in tuple_0:
#                     #                 if isinstance(recurs_1, dict):
#                     #                     print('это если в кей есть кортеж:', tuple_0)
#                     #         elif isinstance(k, dict):
#                     #             dict_1 = (len(k) + (sum(k.values())))
#                     #             print('это если в кей есть словарь:', dict_2)
#                     # # print('это сумма кортежей:', sum(zip(k)))
#
#                     # if isinstance(k,dict):
#                     #     dict_1 = (len(k) + (sum(k.values())))
#                     #     print(k)
#                     #     print(sum(k.values()))
#                     #     print(dict_1)
#
#
#
#
# data_sort(data_structure)
#
# print()
#
# print()
#
# print()
