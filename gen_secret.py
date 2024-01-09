"""
Скрипт, который генерирует манифест secret.

Если на вход access_key подан символ 'g', скрипт генерирует секрет.

requirements:
    pyyaml
    pathlib
"""

import os
import yaml
import random
from pathlib import Path
from base64 import b64encode


# Генерирует случайный секрет (32 байта) а затем энкодит в base64
def gen_secret():
    return b64encode(random.randbytes(32)).decode('utf-8')


def env_fallback(k, prompt='default'):
    if k in os.environ:
        return k
    return input(prompt)

db_pass = env_fallback('SEMAPHORE_DB_PASS', prompt='db_pass(str): ')
admin_pass = env_fallback('SEMAPHORE_ADMIN_PASSWORD', prompt='admin_pass(str): ')
access_key = env_fallback('SEMAPHORE_ACCESS_KEY_ENCRYPTION', prompt='access_key(str/g): ')

if access_key == 'g' or len(access_key) < 8:
    access_key = gen_secret()
    print(f'Секрет: {access_key}\nНастоятельно прошу сохранить его для дальнейших работ')

secret_structure = {
    'apiVersion': 'v1',
    'kind': 'Secret',
    'metadata': {
        'name': 'semaphore-cfg'
    },
    'stringData': {
        'SEMAPHORE_DB_PASS': db_pass,
        'SEMAPHORE_ADMIN_PASSWORD': admin_pass,
        'SEMAPHORE_ACCESS_KEY_ENCRYPTION': access_key
    }
}

with open(Path('manifests')/'secret.yaml', 'w') as yf:
    yaml.dump(secret_structure, yf, default_flow_style=False)