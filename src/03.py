#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 13:11:17
# @Last Modified by: xiepf
# @Last Modified time: 2022-02-06 14:42:25



from def_func import my_abs1,move
import math

from web.student import Student


print(my_abs1(-90))
# print(my_abs1('a'))


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)

r = move(100, 100, 60, math.pi / 6)
print(r)

bart = Student('Bart Simpson', 59)
bart.set_score(100)
bart._Student__score = 10
bart.print_score()
print(bart.name, bart.get_grade())



