#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: xiepf
# @create time: 2022-02-06 16:25:49
# @Last Modified by: xiepf
# @Last Modified time: 2022-02-06 16:41:27
# @description:

class Student(object):
    # 用tuple定义允许绑定的属性名称
    __slots__ = ('name', 'age') 

class GraduateStudent(Student):
    __slots__ = ('grade') 


s = Student() # 创建新的实例
s.name = 'Michael' # 绑定属性'name'
s.age = 25 # 绑定属性'age'

try:
    s.score = 99
except AttributeError as e:
    print('AttributeError:', e)

# s.score = 99 # 绑定属性'score'


# __slots__定义的属性仅对当前类实例起作用，对继承的子类是不起作用
# 子类实例允许定义的属性是自身的__slots__加上父类的__slots__
g = GraduateStudent()
g.name = 'mary'
g.grade = '9年级'
print('g.grade =', g.grade)
print(g.__slots__)


