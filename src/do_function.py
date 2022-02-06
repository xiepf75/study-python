#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 17:53:15
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 17:59:15


print(abs(-10))
f =  abs
print(f(-10))

def add(x, y, f):
    return f(x) + f(y)

x = -5
y = 6

print(add(x,y,f))
