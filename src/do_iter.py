#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Author: xiepf
# @Date:   2022-02-05 16:36:52
# @Last Modified by:   xiepf
# @Last Modified time: 2022-02-05 16:44:51

# 可以直接作用于for循环的数据类型有以下几种：

# 一类是集合数据类型，如list、tuple、dict、set、str等
# 一类是generator，包括生成器和带yield的generator function
# 可以直接作用于for循环的对象统称为可迭代对象：Iterable。
# 使用isinstance()判断一个对象是否是Iterable对象

from collections.abc import Iterable
b = isinstance([], Iterable)
print(b)

isinstance([], Iterable)
isinstance({}, Iterable)
isinstance('abc', Iterable)
isinstance((x for x in range(10)), Iterable)
isinstance(100, Iterable)

# 可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator
# 可以使用isinstance()判断一个对象是否是Iterator对象
isinstance((x for x in range(10)), Iterator)
isinstance([], Iterator)
isinstance({}, Iterator)
isinstance('abc', Iterator)

# 生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator
# list、dict、str等Iterable变成Iterator可以使用iter()函数

