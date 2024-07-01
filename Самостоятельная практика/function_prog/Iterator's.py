# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.


class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __call__(self):
        self.i = 0
        return self

    def __next__(self):
        list_1 = []
        if self.start < self.end:
            for i in range(self.start, self.end):
                if i % 2:
                    list_1.append(i)
                    return list_1
        self.i += 1
        if self.start == None :
            self.start = 0
            return self.start
        else:
            return self.start
        if self.end == None:
            self.end = 1
            return self.end
        else:
            return self.end
        raise StopIteration()

        # def iterate_1(self):
            # list_1 = []
            # if self.start < self.end:
            #     for i in range(self.start, self.end):
            #         if i % 0:
            #             list_1 += i
            #             print(list_1)




result = EvenNumbers(10,25)
test = result.__next__()
print()

print(result)


