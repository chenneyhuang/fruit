import util.mysql_util as ut
from flask import Blueprint
import config


mold = Blueprint('search_info', __name__)

conn = config.conn_str


@mold.route('/', methods=['GET'])
@mold.route('/search_by', methods=['GET'])
def search_by(table, category, value):
    query = 'select * from {} where [{}] = {}'.format(table, category, value)
    df = ut.get_from_db(query, conn)
    return df