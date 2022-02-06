#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: xiepf
# @create time: 2022-02-06 19:41:46
# @Last Modified by: xiepf
# @Last Modified time: 2022-02-06 19:52:15
# @description:

class Animal(object):
    pass

# 大类:哺乳类、鸟类
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 行为类:跑、飞
class Runnable(object):
    def run(self):
        print('Running...')

class Flyable(object):
    def fly(self):
        print('Flying...')

# 各种动物:
# 狗
class Dog(Mammal, Runnable):
    pass

# 蝙蝠
class Bat(Mammal, Flyable):
    pass

# 鹦鹉
class Parrot(Bird, Flyable):
    pass


class RunnableMixIn(object):
    def run(self):
        print('Running...')

# 肉食动物
class CarnivorousMixIn(object):
    pass

# 植食动物
class HerbivoresMixIn(object):
    pass


# 鸵鸟
# 让Ostrich除了继承自Bird外，再同时继承Runnable。这种设计通常称之为MixIn。
class Ostrich(Bird, Runnable, HerbivoresMixIn):
    pass

class Dog(Mammal, RunnableMixIn, CarnivorousMixIn):
    pass


