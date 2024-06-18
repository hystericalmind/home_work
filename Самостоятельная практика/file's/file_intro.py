file_name = 'my_first_file'
file = open(file_name, mode='r',encoding='utf8')
file_data = file.read()
file.close()
print(file_data)




# Создайте переменную с этим файлом
# Распечатайте содержимое текстового файла в консоль, используя оператор with