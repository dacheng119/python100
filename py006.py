#!/usr/bin/env python3
# -*- coding:utf-8 -*-
#斐波那契数列（Fibonacci sequence），又称黄金分割数列、因数学家列昂纳多·斐波那契以兔子繁殖为例子而引入，故又称为“兔子数列”，指的是这样一个数列：1、1、2、3、5、8、13、21、34、在数学上，斐波纳契数列以如下被以递归的方法定义。F(0)=1 F(1)=1 F(n)=F(n-1)+F(n-2) (n>=2)

#题目一：输出第10个斐波纳契数列
def fib1(n):                               #方法一
    a,b=1,1
    for i in range(n-1):
        a,b=b,a+b
    return(a)

def fib2(n):
    if n==1 or n==2:                      #方法二
        return 1
    return fib2(n-1)+fib2(n-2)

print("方法一:第10个数是",fib1(10))
print("方法二:第10个数是",fib2(10))

#题目二：输出指定个数的斐波纳契数列
def fib3(n):
    if n==1:
        return [1]
    if n==2:
        return [1]
    fibs=[1,1]

    for i in range(2,n):
        fibs.append(fibs[i-1]+fibs[i-2])
    return fibs
n=int(input("n=:"))
print("斐波纳契数列的前",str(n),"个数字是：",fib3(n))
