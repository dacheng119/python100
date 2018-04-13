#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#一个整数，它加上100和加上268后都是一个完全平方数。提问：请问该数是多少？
#如果一个正整数 a 是某一个整数 b 的平方，那么这个正整数 a 叫做完全平方数。

import math
for i in range(10000):
    x=int(math.sqrt(i+100))
    y=int(math.sqrt(i+268))
    if(x**2==i+100) and (y**2==i+268):
        print(i)
