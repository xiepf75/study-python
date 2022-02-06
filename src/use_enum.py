#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: xiepf
# @create time: 2022-02-06 19:54:03
# @Last Modified by: xiepf
# @Last Modified time: 2022-02-06 19:58:55
# @description:

from enum import Enum, unique

Month = Enum('Month', ('Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'))

for name, member in Month.__members__.items():
    print(name, '=>', member, ',', member.value)

@unique
class Weekday(Enum):
    Sun = 0 # Sun的value被设定为0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


print(Weekday(1))

