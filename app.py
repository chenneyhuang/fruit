from flask import Flask
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from util.template import ReponseTemplate
from aiohttp import web
from api import import_data, statistic, general_search
import sys
import traceback

app = Flask(__name__)

app.register_blueprint(import_data.mold, url_prefix='/api/import')
app.register_blueprint(general_search.mold, url_prefix='/api/show/<table>/<category>/<value>')
app.register_blueprint(statistic.mold, url_prefix='/api/check')


@app.errorhandler(Exception)
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
        for key,value in json_obj[name]['database'].items():
            os.environ[key] = value


if __name__ == '__main__':
    set_env_by_setting('prod')
    app.run(debug=True)
