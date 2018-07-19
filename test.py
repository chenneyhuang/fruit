import json
import os


# def set_env_by_setting(name):
#     with open("./setting.json") as f:
#         json_obj = json.load(f)
#         if 'extends' in json_obj[name]:
#             extends = json_obj[name]['exends']
#             for key, value in json_obj[extends]['environment_variables'].items():
#                 os.environ[key] = value
#         for key, value in json_obj[name]['environment_variables'].items():
#             os.envrion[key] = value

def check_database():

    print()