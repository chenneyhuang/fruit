import asyncio
import logging
import aiomysql
from sqlalchemy import create_engine
import json
import pandas as pd


# @asyncio.coroutine
# def create_pool(loop, **kw):
#     logging.info('create data base connection pool.....')
#     global __pool
#     __pool = yield from aiomysql.create_pool(
#         host=kw.get('host', 'localhost'),
#         port=kw.get('port', 3306),
#         user=kw['root'],
#         password=kw['root'],
#         db=kw['db'],
#         charset=kw.get('charest', 'utf8'),
#         autocommit=kw.get('autocommit', True),
#         maxsize=kw.get('maxsize', 10),
#         minsize=kw.get('misize', 1),
#         loop=loop
#     )
#
#
# @asyncio.coroutine
# def select(sql, args, size=None):
#     log(sql, args)
#     global __pool
#     with (yield from __pool) as conn:
#         cur = yield from conn.cursor(aiomysql.DictCursor)
#         yield from cur.excute(sql.replace('?', '%s'), args or ())
#         if size:
#             rs = yield from cur.fetchmany(size)
#         else:
#             rs = yield from cur.fetchall()
#         yield from cur.close()
#         logging.info('rows returned: %s' % len(rs))
#         return rs


def get_from_db(query, conn, params=None):
    df = pd.read_sql(query, conn, params=params)
    df.fillna('', inplace=True)
    return df


def read_excel(file_fullpath):

    return pd.read_sql(file_fullpath)
