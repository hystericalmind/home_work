def all_variants(text):
    res_1 = ''
    for i in text:
        yield i
    if len(text) > 0 :
        yield (f'{text[0]}{text[1]}\n{text[1]}{text[2]}')
    for k in text:
        yield text
        break


func_txt = all_variants(text='abc')

for res in func_txt:
    print(res)
