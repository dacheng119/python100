#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#要求输入某年某月某日。求判断输入日期是当年中的第几天？
year=int(input("年："))
month=int(input("月："))
day=int(input("日："))

months=(0,31,59,90,120,151,181,212,243,273,304,334)   #这个元组真是很犀利啊
if 0<month<=12:
    sum=months[month-1]
else:
    print("date error")
sum += day

runNianFlag=0                             #设置润年标志位
if(year % 400==0) or((year % 4 ==0)and(year % 100 !=0)):
    runNianFlag=1
if(runNianFlag==1) and(month>2):
    sum +=1                               #润年里3－12月要多一天
print("它是第%d天." %sum)

    
