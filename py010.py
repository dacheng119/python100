#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#题目：暂停一秒输出格式化后的当前时间
"""time.time()函数的作用：返回自Unix纪元以后的秒数，是一个浮点数
time.localtime()函数的作用：把一个浮点数转化为一个元组，其中共有9个元素
time.strftime()函数的作用：把一个时间元组转化为一个字符串，其格式由format字符串指定"""
import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))) #检测括号最简单的办法是数一数。看有几个左小括号，又有几个右小括号
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))


