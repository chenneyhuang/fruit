import json
import os
import os
import json
import pandas as pd
from sqlalchemy import create_engine
from model.dbmodel import Customers, Transaction
from sqlalchemy import Table, MetaData, Column, Integer, String
from sqlalchemy.orm import mapper, sessionmaker
import config
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

conn = config.conn_str


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


def tran_test():
    #print(conn)
    engine = create_engine(conn)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    transaction_obj = Transaction(name="chenney2", date="2016-02-14", product="xxxx2",
                                  quantity=11, amount=15.48)

    session.add(transaction_obj)
    session.commit()


if __name__ == '__main__':
    # set_env_by_setting('prod')
    # conn_str = os.environ.get('ConnectionString')
    # print(conn_str)
    # test_uploaded_file("-1.xlsx")
    tran_test()


# def check_database():
#
#     print()