#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 19:32:10
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 19:43:11

# 当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数
def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum

# 调用函数f时，才真正计算求和的结果：
f = lazy_sum(1, 3, 5, 7, 9)
print(f())


# 每次循环，都创建了一个新的函数，然后，把创建的3个函数都返回了。
def count():
    fs = []
    for i in range(1, 4):
        def f():
             return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())


# fix:
def count():
    fs = []
    def f(n):
        def j():
            return n * n
        return j
    for i in range(1, 4):
        fs.append(f(i))
    return fs

f1, f2, f3 = count()

print(f1())
print(f2())
print(f3())

