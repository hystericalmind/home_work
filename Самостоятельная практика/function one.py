def function_one(num_1,*num_2):
    num_1 = int(input('input number 1: '))
    print(f'Your num #1 is : {num_1}!')
    for i in num_2:
        num_2 = int(input('i need number 2, now!!! input: '))
        if num_2 > 1000:
            print(num_1 * num_2)
        elif num_2 < 1000:
            print('Error')



function_one(1, 99 )
function_one(1, 1000, 90, 21)