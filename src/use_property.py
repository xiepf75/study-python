#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: xiepf
# @create time: 2022-02-06 16:42:09
# @Last Modified by: xiepf
# @Last Modified time: 2022-02-06 16:48:13
# @description:

'''
class Student(object):

    def get_score(self):
         return self._score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value
'''

class Student(object):
    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    @property
    def age(self):
        return 2021 - self._birth

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('score must be an integer!')
        if value < 0 or value > 100:
            raise ValueError('score must between 0 ~ 100!')
        self._score = value 

s = Student()
s.score = 60 # OK，实际转化为s.set_score(60)
s.score
print(s.score)

try:
    s.score = 9999
except AttributeError as e:
    print('AttributeError:', e)

