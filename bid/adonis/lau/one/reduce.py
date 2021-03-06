#!/usr/bin/env python3
# -*- coding:utf-8 -*-

from functools import reduce

list_var = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def add(x, y):
    return x + y


print(reduce(add, list_var))


def fn(x, y):
    return x * 10 + y


print(reduce(fn, list_var))


def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]


print(reduce(fn, map(char2num, '123456789')))


def str2int(s):
    def fn(x, y):
        return x * 10 + y

    def char2num(s):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

    return reduce(fn, map(char2num, s))


print(str2int('123456789987654321'))


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))


print(str2int('852741963'))


