# Напишите класс-итератор EvenNumbers для перебора чётных чисел в определённом числовом диапазоне.


class EvenNumbers:

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.i = 0

    def __iter__(self):
        self.i = 0
        return self

    def __next__(self):
        list_1 = []
        if self.start < self.end:
            for i in range(self.start, self.end):
                if i % 2 == 0:
                    list_1.append(i)
                    continue
            return list_1
        if self.start == None :
            self.start = 0
            return self.start
        if self.end == None:
            self.end = 1
            return self.end

        raise StopIteration()



result = EvenNumbers(10,25)
test = result.__next__()
print()
for i in test:
    print(i)

