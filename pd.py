#!/usr/bin/env python
#-*- coding:utf-8 -*-

#author:maxiunan
from datetime import datetime
import pandas as pd

data = {"calories":['c','a','b'],
        "实际时间":['2022-01-02 00:00:00','2022-02-09 13:12:34','2022-06-09 13:12:34'],
        '计划时间':['2022-01-01 00:00:00','2022-03-09 13:12:34','2022-06-09 13:32:34'],
        "num1":[34,78,None],
        "num2":[25,37,100]}
df = pd.DataFrame(data)
print(df)
# print(type(df[['duration','plan_time']]))
def format_colnum(*name):
    for na in name:
        df[na] = pd.to_datetime(df[na], format='%Y-%m-%d %H:%M:%S')
format_colnum('实际时间', '计划时间')
# 筛选出实际时间<计划时间的数据

cond1 = (df["实际时间"] < df['计划时间']) & (df['num1'] > df['num2'])

print(df[cond1])
# print(df['num1'].sum(skipna = True))
# print(df.describe())
# print(df.dtypes)
# print(df.count())

# print(df['calories']<df['actual_time'])
# print(type(df.loc[0]))
# print(df[df['calories']>33])
# print(df.loc[1])
# print(type(df['calories']))
# print(df['actual_time']>datetime(2022,1,1))
#


# for i in df.index:
#     if( isinstance(df.loc[i, "v"],str)):
#         df.loc[i, "actual_time"] = datetime.strptime(df.loc[i, "actual_time"], '%Y-%m-%d %H:%M:%S')
#         print(type(df.loc[i, "actual_time"]))
#         print(df.loc[i, "actual_time"] > datetime(2022,1,1))
#
# print(df['duration'])

# df['new'] = df['num1'] / df['num2']
#
# print(df)
#

