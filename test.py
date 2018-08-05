import json
import os
import os
import json
import pandas as pd


def set_env_by_setting(name):
    with open("./setting.json") as f:
        json_obj = json.load(f)
        print(f)
        print(json_obj)
        # db = json_obj[name]['database']
        for key,value in json_obj[name]['database'].items():
            os.environ[key] = value
            print(os.environ.get('ConnectionString'))

def test_uploaded_file(file):
    df = pd.read_excel(file)
    return df.info()

if __name__ == '__main__':
    # set_env_by_setting('prod')
    # conn_str = os.environ.get('ConnectionString')
    # print(conn_str)
    test_uploaded_file("-1.xlsx")



# def check_database():
#
#     print()