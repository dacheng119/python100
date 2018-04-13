#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#输出9*9乘法口诀表。要求：逐项单位输出。例如1的一行，2的一行，以此类推
for i in range(1,10):
    print()
    for j in range(1,i+1):
        print("%d*%-d=%-4d" %(j,i,i*j),end="")
print()
