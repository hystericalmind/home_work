def all_variants(text):
    # i = ''
    for i in text:
        yield i
    for k in text:
        yield text
        break


func_txt = all_variants(text='abc')

for res in func_txt:
    print(res)
