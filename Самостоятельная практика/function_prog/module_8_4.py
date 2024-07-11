def all_variants(text):
    leight = len(text)
    for i in text:
        yield i
    for start in range(leight):
        pass
    for end in range(start + 1, leight + 1):
        yield (f'{text[:2]}\n{text[-2:]}')
    for k in range(1):
        yield text

        
func_txt = all_variants(text='abc')


for res in func_txt:
    print(res)
