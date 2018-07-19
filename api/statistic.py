import simplejson as json
from flask import Blueprint, request
from util.template import ReponseTemplate

mold = Blueprint('selling_info', __name__)

@mold.route('/', methods=['GET'])
@mold.route('/index', methods=['GET'])
def show_selling_info():
    pass

