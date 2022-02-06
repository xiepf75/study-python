#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @author: xiepf
# @create time: 2022-02-06 20:18:17
# @Last Modified by: xiepf
# @Last Modified time: 2022-02-06 20:19:01
# @description:

class Dict(dict):

    def __init__(self, **kw):
        super().__init__(**kw)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError(r"'Dict' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value
