#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#任意三个整数类型，x、y、z。要求把这三个数，按照由小到大的顺序输出
l=[]
for i in range(3):
    j=int(input("i=:"))
    l.append(j)
l.sort()
print(l)
