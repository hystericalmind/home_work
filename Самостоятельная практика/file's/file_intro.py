file_name = 'my_first_file'
file = open(file_name, mode='r',encoding='utf8')
file_data = file.read()
file.close()
print(file_data)