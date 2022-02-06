#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 15:49:43
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 16:12:30


n = list(range(1, 11))

print(n)


'''
L = []
for x in range(1, 11):
    L.append(x*x)
print(L)
'''

n1 = [x * x for x in range(1, 11)]
print(n1)

n2 = [x * x for x in range(1, 11) if x % 2 == 0]
print(n2)

n3 = [m + n for m in 'ABC' for n in 'XYZ']
print(n3)

d = {'x': 'A', 'y': 'B', 'z': 'C' }
n4 = [k + '=' + v for k, v in d.items()]
print(n4)

L = ['Hello', 'World',155,'IBM', 'Apple']
n5 = [s.lower() for s in L if isinstance(s, str) == True]
print(n5)

