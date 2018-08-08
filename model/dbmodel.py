# -*- coding:utf-8 -*-

from sqlalchemy import Table, MetaData, Column, Integer, String, DATE, DECIMAL, ForeignKey, DateTime
from sqlalchemy.orm import mapper
from sqlalchemy.ext.declarative import declarative_base

#metadata = MetaData()
Base = declarative_base()

# customers = Table('customers', metadata,
#                   Column('id', Integer, primary_key=True, autoincrement=True),
#                   Column('name', String(20)),
#                   Column('phone', String(20)),
#                   Column('address', String(45)),
#                   Column('source_from', String(45))
#                   )


class Customers(Base):
    # def __init__(self, id, name, phone, address, source_from):
    #     self.id = id
    #     self.name = name
    #     self.phone = phone
    #     self.address = address
    #     self.source_from = source_from
    #
    # def __repr__(self):
    #     return "<Customer(name='%s', phone='%s', address='%s', " \
    #            "source_from='%s')" % (self.name, self.phone, self.address,
    #                                   self.source_from)
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(20))
    phone = Column(String(20))
    address = Column(String(45))
    source_from = Column(String(45))

# mapper(Customers, customers)

# 类关联起来
# the table metadata is created separately with the Table construct,
# then associated with the User class via the mapper() function
# 如果数据库里有，就不会创建了。

# transaction = Table('transaction', metadata,
#                     Column('id', Integer, primary_key=True, autoincrement=True),
#                     Column('name', String(20)),
#                     Column('date', DateTime),
#                     Column('product', String(20)),
#                     Column('quantity', Integer),
#                     Column('amount', DECIMAL(2))
#                     )


class Transaction(Base):
    # def __init__(self, id, name, date, product, quantity, amount):
    #     self.id = id
    #     self.name = name
    #     self.date = date
    #     self.product = product
    #     self.quantity = quantity
    #     self.amount = amount
    #
    # def __repr__(self):
    #     return "<Transaction(name='%s', date='%s', product='%s'," \
    #            "quantity='%s', amount='%s')>" % (self.name, self.date,
    #                                              self.product, self.quantity,
    #                                              self.amount)
    __tablename__ = 'transaction'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(20))
    date = Column(DATE)
    product = Column(String(20))
    quantity = Column(Integer)
    amount = Column(Integer)

# mapper(Transaction, transaction)

