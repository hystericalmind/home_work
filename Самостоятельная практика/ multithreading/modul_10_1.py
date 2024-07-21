import threading
from time import sleep
import datetime
from threading import Thread


file_names = 'examplel1.txt'

def wite_words(word_count, file_name):
     with open(file_name, mode='a', encoding='utf8') as f:
        for i in range(word_count):
            f.writelines(f'Какое-то слово № {i}\n')
            sleep(0.1)
        print(f'Завершилась запись в файл: {file_name} ')

start_1 = datetime.datetime.now()

wite_words(10,'examplel1.txt')
wite_words(30,'examplel2.txt')
wite_words(200,'examplel3.txt')
wite_words(100,'examplel4.txt')

finish_1 = datetime.datetime.now()
print(f'Работа потоков: {finish_1 - start_1}')

start_2 = datetime.datetime.now()

threading.Thread(target=wite_words(10,'examplel5.txt'),daemon=False).start()
threading.Thread(target=wite_words(30,'examplel6.txt'),daemon=False).start()
# threading.Thread(target=wite_words(200,'examplel7.txt'),daemon=False).start()
threading.Thread(target=wite_words(100,'examplel8.txt'),daemon=False).start()



finish_2 = datetime.datetime.now()
print(f'Работа потоков: {finish_2 - start_2}')

# f_1.start()
# f_2.start()
# f_3.start()
# f_4.start()

# f_1.join()
# f_2.join()
# f_3.join()
# f_4.join()

