# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 15:26
# @Author  : wenchuan
# @Email   : 139718362@qq.com
# @File    : Stock.py
# @Software: PyCharm


from jqdatasdk import *
import time
import pandas as pd

# 设置行列不忽略
pd.set_option('display.max_rows', 5000)
pd.set_option('display.max_columns', 10)

auth('17621171968', '171968')

# 查询今日剩余查询数
# count=get_query_count()
# print(count)

'''resample函数的使用'''

# 转换周期: 日K转换为周K
# df = get_price('000001.XSHG', count=20, end_date='2021-02-22',
#                frequency='daily', panel=False)  # 获取日K
#
#
# # 获取周K（当周的）：开盘价（当周第一天）、收盘价（当周最后一天）、最高价（当周）、最低价（当周）
# df_week = pd.DataFrame()
# df_week['open'] = df['open'].resample('W').first()
# df_week['close'] = df['close'].resample('W').last()
# df_week['high'] = df['high'].resample('W').max()
# df_week['low'] = df['low'].resample('W').min()
#
#
# # 汇总统计：统计一个月成交量、成交额（sum）
# df_week['volume(sum)'] = df['volume'].resample('w').sum()
# df_week['money(sum)'] = df['money'].resample('w').sum()
#
#
# print(df_week)

'''获取股票财务指标'''
df = get_fundamentals(query(indicator), statDate='2020')  # 获取财务指标数据
# df.to_csv('finance2020.csv')
#
# # 基于盈利指标选股：eps, operating_profit,roe,inc_total_revenue_year_on_year
operating_profit_average = df['operating_profit'].mean()  # 净收益大于平均值的

df = df[(df['eps'] > 0) & (df['operating_profit'] > operating_profit_average) &
        (df['roe'] > 11) & (df['inc_total_revenue_year_on_year'] > 10)]

# print(df['code'], len(df))

'''获取股票估值指标'''
df_valuation = get_fundamentals(query(valuation), statDate='2020')
print(df_valuation.head())

# df_valuation中pe_ratio加入到df中，以code拼接
df.index = df['code']
df_valuation.index = df_valuation['code']
df['pe_ratio'] = df_valuation['pe_ratio']
df = df[df['pe_ratio'] < 50]
print(df.head())

