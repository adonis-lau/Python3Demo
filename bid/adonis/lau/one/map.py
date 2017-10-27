#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list_var = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def f(x):
    return x * x


map_re_1 = map(f, list_var)

print(map_re_1)
# 由于结果r是一个Iterator，Iterator是惰性序列，因此通过list()函数让它把整个序列都计算出来并返回一个list。
print(list(map_re_1))

map_re_2 = map(str, list_var)
print(map_re_2)
print(list(map_re_2))
