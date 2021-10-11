import json

from tinydb import TinyDB, Query
import requests

db = TinyDB('db.json')

for i in db.all():
    print(i)

Tariff = Query()
result = db.search(Tariff.Cells.NameOfTariff == 'Банковская карта с технологией бесконтактной оплаты')

for i in result:
    print(i)
# r = requests.get('https://apidata.mos.ru/v1/datasets/658/rows?api_key=467a5fb6e2750e7a87f02e947799ec3e')
# r.encoding = 'utf-8'
# json_data = json.loads(r.text)
#
# print(json_data)
# for i in json_data:
#     print(i)
#     db.insert(i)

