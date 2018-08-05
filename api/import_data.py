import json
from flask import Blueprint, request
from util.template import ReponseTemplate
import logging
from model.dbmodel import Customers, Transaction
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import create_engine
import config
import pandas as pd

mold = Blueprint('import', __name__)

conn = config.conn_str


@mold.route('/customer', methods=['POST'])
def import_customer():
    engine = create_engine(conn)
    #df = pd.read_excel(request.data)
    cum = json.loads(request.data)
    if cum is None:
        logging.info("Not able to get the data from request.")
    # Customers.name = cum.get('name', '')
    # Customers.address = cum.get('address', '')
    # Customers.phone = cum.get('phone', '')
    # Customers.source_from = cum.get('source_from', '')
    name = cum.get('name', '')
    address = cum.get('address', '')
    phone = cum.get('phone', '')
    source_from = cum.get('source_from', '')

    # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    Session_class = sessionmaker(bind=engine) # 实例和engine绑定
    Session = Session_class # 生成session实例，相当于游标
    # generate the object for the data we would like to insert
    customer_obj = Customers(name=name, address=address,
                             phone=phone, source_from=source_from)
    # nothing yet, print to check
    print(customer_obj.id, customer_obj.name,
          customer_obj.phone, customer_obj.address,
          customer_obj.source_from)

    Session.add(customer_obj)  # put the data obj into session, will insert together
    # check again. but still nothing yet....
    print(customer_obj.id, customer_obj.name,
          customer_obj.phone, customer_obj.address,
          customer_obj.source_from)
    Session.commit()  # insert the data into database
    return ReponseTemplate.jsonify_ok_obj_response(customer_obj)


@mold.route('/transactions/', methods=['POST'])
def import_transactions(file_name):
    engine = create_engine(conn)
    #df = pd.read_excel(request.data)
    #tran = json.loads(request.data)
    tran = pd.read_excel(file_name)
    if tran is None:
        logging.info("Not able to get the data from request.")
    name = tran.get('客户姓名', '')
    date = tran.get('交易日期', '')
    product = tran.get('产品名称', '')
    quantity = tran.get('成交量', '')
    amount = tran.get('成交金额', '')

    # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    Session_class = sessionmaker(bind=engine)  # 实例和engine绑定
    Session = Session_class  # 生成session实例，相当于游标
    # generate the object for the data we would like to insert

    transaction_obj = Transaction(name=name, date=date, product=product,
                                  quantity=quantity, amount=amount)
    # print to check, there should be nothing yet
    print(transaction_obj.name, transaction_obj.product, transaction_obj.date,
          transaction_obj.quantity, transaction_obj.amount)
    Session.add(transaction_obj) # put the data into obj
    # check again, three should be nothing still
    print(transaction_obj.name, transaction_obj.product, transaction_obj.date,
          transaction_obj.quantity, transaction_obj.amount)
    Session.commit() # insert
    return ReponseTemplate.jsonify_ok_obj_response(transaction_obj)


@mold.route('/test', methods=['POST'])
def test():
    # test1 = request.form
    # dict = test1.to_dict()
    # # test2.info()
    # print(dict)
    test1 = request.files
    print(test1)
    test2 = test1.to_dict(flat=False)

    print(test2)
    test3 = request.data
    print(test3)



    return ReponseTemplate.jsonify_ok_obj_response(test2)