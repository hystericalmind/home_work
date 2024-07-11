import requests


THE_URL = 'https://ya.ru/'
res = []

for i in range(2):
    response = requests.get(THE_URL)
    page_respinse = response.json()
    res.append(page_respinse)

print(res)