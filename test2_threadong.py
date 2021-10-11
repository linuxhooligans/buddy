import json
import os
from multiprocessing import Pool
import requests


def f():
    print('parrentid:',os.getppid(),'processid:', os.getpid())
    r = requests.get('http://jsonplaceholder.typicode.com/posts')
    json_data = json.loads(r.text)
    print(json_data)

if __name__ == '__main__':
    with Pool() as pool:
        for i in range(20):
            result = pool.apply_async(f,)
        pool.close()
        pool.join()