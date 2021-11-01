# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 15:29
# @Author  : wenchuan
# @Email   : 139718362@qq.com
# @File    : stock.py
# @Desc    : main
from jqdatasdk import *
import time
import pandas as pd
import os


def get_stock_list():
    """
    获取所有A股股票列表；
    上海证券交易所.XSHG
    深圳证券交易所.XSHE
    :return: stock_list
    """
    stock_list = list(get_all_securities(['stock']).index)
    return stock_list


def get_single_price(code, time_freq, start_date, end_date):
    """
    获取单个股票行情数据
    :param code:
    :param time_freq:
    :param start_data:
    :param end_date:
    :return:
    """
    data = get_price(code, start_date=start_date, end_date=end_date,
                     frequency=time_freq, panel=False)
    return data


def export_data(data, filename, type):
    """
    导出股票相关数据到本地csv文件
    :param data:
    :param filename:
    :param type: 股票数据类型，可以是：price、finance
    :return:
    """
    
    file_root = '../data/' + type + '/' + filename + '.csv'
    data.index.names = ['date']
    data.to_csv(file_root, mode='a')
    print("已成功存储至：", file_root)


def transfer_price_freq(data, time_freq):
    """
    将数据转换为制定周期：开盘价（周期第一天）、收盘价（周期最后一天）、最高价（周期内）、最低价（周期内）
    :param data:
    :param time_freq:
    :return:
    """

    df_trans = pd.DataFrame()
    df_trans['open'] = data['open'].resample(time_freq).first()
    df_trans['close'] = data['close'].resample(time_freq).last()
    df_trans['high'] = data['high'].resample(time_freq).max()
    df_trans['low'] = data['low'].resample(time_freq).min()

    return df_trans


def get_single_finance(code, date, statDate):
    """
    获取单个股票财务指标
    :param code:
    :param date:
    :param statDate:
    :return:
    """
    data = get_fundamentals(query(indicator).filter(indicator.code == code), date=date, statDate=statDate)
    return data


def get_sing_valuation(code, date, statDate):
    """
    获取单个股票估值指标
    :param code:
    :param date:
    :param statDate:
    :return:
    """
    data = get_fundamentals(query(valuation).filter(valuation.code == code), date=date, statDate=statDate)
    return data




