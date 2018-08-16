# -*- coding:utf-8 -*-

import json
from flask import Blueprint, request
from util.template import ResponseTemplate
import logging
from model.dbmodel import Customers, Transaction
from sqlalchemy.orm import mapper, sessionmaker
from sqlalchemy import create_engine
import config
import pandas as pd
from sqlalchemy.ext.declarative import declarative_base
import xlrd
import time
import datetime

mold = Blueprint('import', __name__)

conn = config.conn_str
Base = declarative_base()


@mold.route('/customer', methods=['POST'])
def import_customer():
    engine = create_engine(conn)
    # df = pd.read_excel(request.data)
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

    Base.metadata.create_all(engine)
    # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    Session_class = sessionmaker(bind=engine)  # 实例和engine绑定
    session = Session_class()  # 生成session实例，相当于游标
    # generate the object for the data we would like to insert
    customer_obj = Customers(name=name, address=address,
                             phone=phone, source_from=source_from)
    # nothing yet, print to check
    print(customer_obj.id, customer_obj.name,
          customer_obj.phone, customer_obj.address,
          customer_obj.source_from)
    session.add(customer_obj)  # put the data obj into session, will insert together
    # check again. but still nothing yet....
    print(customer_obj.id, customer_obj.name,
          customer_obj.phone, customer_obj.address,
          customer_obj.source_from)
    session.commit()  # insert the data into database
    return ResponseTemplate().jsonify_ok_obj_response(customer_obj)


@mold.route('/transactions/<file_name>', methods=['POST'])
def import_transactions(file_name):
    engine = create_engine(conn)

    #df = pd.read_excel(request.data)
    #tran = json.loads(request.data)
    #tran = pd.read_excel(file_name)
    book = xlrd.open_workbook(file_name)
    # tran = book.sheet_by_index(0)
    tran = book.sheet_by_name("Sheet1")

    Base.metadata.create_all(engine)
    # 创建与数据库的会话session class ,注意,这里返回给session的是个class,不是实例
    Session_class = sessionmaker(bind=engine)  # 实例和engine绑定
    session = Session_class()  # 生成session实例，相当于游标
    #
    rowList= tran.row_values(1)

    columns = ['name', 'date', 'product', 'quantity', 'amount']
    index = []
    df = pd.DataFrame(index=index, columns=columns)
    for r in range(1, tran.nrows):

    # if tran is None:
    #     logging.info("Not able to get the data from file.")
    # name = tran.get('客户姓名', '')
    # # print(name)
    # date = tran.get('交易日期', '')
    # # print(date)
    # product = tran.get('产品名称', '')
    # # print(product)
    # quantity = tran.get('成交量', '')
    # amount = tran.get('成交金额', '')
        name = tran.cell(r,0).value
        date = datetime.datetime(*time.strptime("Dec 30 1899", "%b %d %Y")[:6]) + \
        datetime.timedelta(days=int(rowList[1]))
        #print(type(date))
        product = tran.cell(r,2).value
        quantity = tran.cell(r,3).value
        amount = tran.cell(r,4).value

        # generate the object for the data we would like to insert

        transaction_obj = Transaction(name=name, date=date, product=product,
                                      quantity=quantity, amount=amount)

        df1 = pd.DataFrame([[name, date, product, quantity, amount]], columns=columns)

        df = df.append(df1)
        # print(type(transaction_obj.name))

        # s = json.dumps(transaction_obj)
        # print to check, there should be nothing yet
        print(transaction_obj.name, transaction_obj.product, transaction_obj.date,
              transaction_obj.quantity, transaction_obj.amount)
        session.add(transaction_obj)  # put the data into obj
    # check again, there should be nothing still
    print(transaction_obj.name, transaction_obj.product, transaction_obj.date,
          transaction_obj.quantity, transaction_obj.amount)
    session.commit()  # insert
    return ResponseTemplate().jsonify_ok_df_response(df)


# @mold.route('/test', methods=['POST'])
# def test():
#     # test1 = request.form
#     # dict = test1.to_dict()
#     # # test2.info()
#     # print(dict)
#     test1 = request.files
#     print(test1)
#     test2 = test1.to_dict(flat=False)
#
#     print(test2)
#     test3 = request.data
#     print(test3)
#
#     return ReponseTemplate.jsonify_ok_obj_response(test2)