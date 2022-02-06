#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 19:11:40
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 19:15:46

# filter()也接收一个函数和一个序列,
# 和map()不同的是，filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。
# 要强迫filter()完成计算结果，需要用list()函数获得所有结果并返回list。

# 在一个list中，删掉偶数，只保留奇数
def is_odd(n):
    return n % 2 == 1

n = list(filter(is_odd, [1, 2, 4, 5, 6, 9, 10, 15]))
print(n)


# 把一个序列中的空字符串删掉
def not_empty(s):
    return s and s.strip()

n = list(filter(not_empty, ['A', '', 'B', None, 'C', '  ']))
print(n)




