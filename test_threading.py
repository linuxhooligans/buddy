import json
from multiprocessing import Process
import uuid
import os
import requests

def f(name):
    print('parrentid:',os.getppid(),'processid:', os.getpid())
    r = requests.get('https://apidata.mos.ru/v1/datasets/658/rows?api_key=467a5fb6e2750e7a87f02e947799ec3e')
    json_data = json.loads(r.text)
    print(json_data)

if __name__ == '__main__':
    # for i in range(4):
        uuid_tmp = uuid.uuid4()
        p = Process(target=f, args=(uuid_tmp,))
        p.start()
        p.join()

