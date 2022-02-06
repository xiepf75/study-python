#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 16:14:36
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 16:35:41

# 把一个列表生成式的[]改成()，创建一个generator
L = [x * x for x in range(10)]
print(L)

g = (x * x for x in range(10))
print(g)
print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)

# 斐波拉契数列用列表生成式
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

f = fib(10)
print('fib(10):', f)
for x in f:
    print(x)


g = fib(5)
while 1:
    try:
        x = next(g)
        print('g:', x)
    except StopIteration as e:
        print('Generator return value:', e.value)
        break
