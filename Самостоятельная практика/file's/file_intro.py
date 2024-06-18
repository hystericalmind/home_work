file_name = 'my_first_file'
file = open(file_name, mode='r',encoding='utf8')
file_data = file.read()
while file_data:
    if 'my' in file_data:
        print(file_data)
        break
file.close()





# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль, используя оператор with