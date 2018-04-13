#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#题目要求：请输出使用1 2 3 4四个数字组成的互不相同且无重复数字的三位数字。
[print(str(i)+str(j)+str(k)) for i in  range(1,5) for  j in range(1,5) for k in range(1,5) \
     if i != j and i !=k and j !=k ]
