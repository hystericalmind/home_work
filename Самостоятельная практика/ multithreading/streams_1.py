from threading import Thread
from time import sleep

alphabet = [chr(i) for i in range(97, 123)]
list_1 = list(range(1, 11))



def stream_1(*args):
    for i in args:
        # for j in i:
        print(i)
        sleep(1)

def stream_2(*args):
    for i in args:
        if i != 'k':
            print(i)
            sleep(1)
        else:
            break
#
func_1 = Thread(target=stream_1, args= list_1)
func_2 = Thread(target=stream_2, args= alphabet)

func_1.start()
func_2.start()

func_1.join()
func_2.join()
