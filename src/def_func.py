# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 12:35:21
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 13:03:45


#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

def my_abs(x):
  if x >= 0:
    return x
  else:
    return -x


def my_abs1(x):
  # 数据类型检查可以用内置函数isinstance()
  if not isinstance(x, (int, float)):
      raise TypeError('bad operand type')
  if x >= 0:
      return x
  else:
    return -x

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny

n = my_abs1(-90)
print(n)
# TypeError: bad operand type:
# print(my_abs1('a'))


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)