# -*- coding:utf-8 -*-
import pandas as pd
from flask import Flask, request
import logging; logging.basicConfig(level=logging.INFO)
import asyncio, os, json, time
from datetime import datetime
from util.template import ReponseTemplate
from aiohttp import web
from api import import_data, statistic, general_search
import sys
import traceback
from werkzeug.utils import secure_filename

# UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = set(['xlsx', 'xls', 'csv'])
app = Flask(__name__)
# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 60 * 1024 * 1024

app.register_blueprint(import_data.mold, url_prefix='/api/import')
app.register_blueprint(general_search.mold, url_prefix='/api/show/<table>/<category>/<value>')
app.register_blueprint(statistic.mold, url_prefix='/api/check')


def allowed_file(filename):
    return '.' in filename and \
        filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/upload', methods=['POST'])
def upload_excel():
    f = request.files['file']
    if f and allowed_file(f.filename):
        filename = secure_filename(f.filename)
        f.save(secure_filename(filename))
        # file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        df = pd.read_excel(f)
        return ReponseTemplate().jsonify_ok_df_response(df)


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
