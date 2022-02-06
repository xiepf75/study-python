#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 20:05:45
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 20:16:26


n = list(map(lambda x: x * x, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(n)

# 匿名函数lambda x: x * x实际上就是：
def f(x):
    return x * x

f1 = lambda x: x * x
print(f1(5))

# 把匿名函数作为返回值返回，比如：
def build(x, y):
    return lambda: x * x + y * y
f2 = build(5,2)
print(f2())


def is_odd(n):
    return n % 2 == 1

L1 = list(filter(is_odd, range(1, 20)))

L2 = list(filter(lambda x: x % 2 == 1, range(1, 20)))
print(L1)
print(L2)



