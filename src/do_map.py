#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 18:00:42
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 18:06:14


# map()函数接收两个参数，一个是函数，一个是Iterable，map将传入的函数依次作用到序列的每个元素，并把结果作为新的Iterator返回。

# 函数f(x)=x^2
def f(x):
    return x * x


r = map(f,[1,2,3,4,5,6,7,8,9])
print(list(r))


# 把ist所有数字转为字符串：
s = list(map(str, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(s)
