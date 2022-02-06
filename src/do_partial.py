#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 21:49:25
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 21:58:43

# 偏函数
import functools

int2 = functools.partial(int, base=2)

print('1000000 =', int2('1000000'))
print('1010101 =', int2('1010101'))

# 当函数的参数个数太多，需要简化时，使用functools.partial可以创建一个新的函数，这个新函数可以固定住原函数的部分参数，从而在调用时更简单。

args = (10, 5, 6, 7)
n1 = max(*args)
print(n1)

max2 = functools.partial(max, 10)
n2 = max2(5, 6, 7)
print(n2)

int2 = functools.partial(int, base=2)
n3 = int2('10010')
print(n3)

# 相当于
kw = { 'base': 2 }
int('10010', **kw)


