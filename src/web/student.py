#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: xiepf
# @create_time:   2022-02-05 22:31:14
# @Last Modified by: xiepf
# @Last Modified time: 2022-02-06 14:14:14
# @description:

class Student(object):
    def __init__(self, name, score,sex='F'):
        self.name = name
        self.__score = score
        self.__sex = sex

    def get_sex(self):
        return self.__sex

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
        else:
            raise ValueError('bad score')

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

    def print_score(self):
        print('%s: %s %s' % (self.name, self.__sex,self.__score))