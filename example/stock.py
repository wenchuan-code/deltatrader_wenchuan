# -*- coding: utf-8 -*-
# @Time    : 2021/11/1 16:15
# @Author  : wenchuan
# @Email   : 139718362@qq.com
# @File    : stock.py
# @Desc    : 用于调用股票行情数据的脚本

import data.stock as st
import os


# 初始化变量
code = '000002.XSHE'

# 调用一只股票的行情数据
data = st.get_single_price(code=code, time_freq='daily', start_date='2021-02-01', end_date='2021-03-01')

# 存入csv
st.export_data(data=data, filename=code, type='price')

print(data)

# 实时更新数据

