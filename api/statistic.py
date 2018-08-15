# -*- coding:utf-8 -*-

import simplejson as json
from flask import Blueprint, request
from sqlalchemy import create_engine
import config
from sqlalchemy.orm import sessionmaker
from util.template import ResponseTemplate
from model.dbmodel import Transaction
import util.mysql_util as ut

mold = Blueprint('selling_info', __name__)

conn = config.conn_str


@mold.route('/', methods=['GET'])
@mold.route('/by_product', methods=['GET'])
def by_product(product):
    engine = create_engine(conn)
    Session_class = sessionmaker(bind=engine)
    Session = Session_class()
    selling_detail = Session.query(Transaction.Transaction).filter_by(product='{}'.format(product)).all
    return ResponseTemplate.jsonify_ok_obj_response(selling_detail)
