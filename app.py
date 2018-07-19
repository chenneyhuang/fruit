from flask import Flask
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from util.template import ReponseTemplate
from aiohttp import web
from api import import_data, statistic
import sys
import traceback

app = Flask(__name__)

app.register_blueprint(import_data.mold, url_prefix='/import')


@app.error_handler(Exception)
def default_exception_handler(error):
    exc_type, exc_value, exc_traceback = sys.exc_info()
    trace = traceback.format_exception(exc_type, exc_value,
                                       exc_traceback)
    code = 401 if 'auth' in str(type(error)).lower() else 400
    print('[Error]:{}'.format(trace))

    return ReponseTemplate().jsonify_bad_response(str(error), code)


def set_env_by_setting(name):
    with open("./setting.json") as f:
        json_obj = json.load(f)
        # db = json_obj[name]['database']
        for key,value in json_obj[name]['database']:
            os.environ[key] = value


if __name__ == '__main__':
    app.run(debug=True)