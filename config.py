import os
import json


def set_env_by_setting(name):
    with open("./setting.json") as f:
        json_obj = json.load(f)
        print(f)
        print(json_obj)
        # db = json_obj[name]['database']
        for key,value in json_obj[name]['database'].items():
            os.environ[key] = value


set_env_by_setting('prod')
conn_str = os.environ.get('ConnectionString')

