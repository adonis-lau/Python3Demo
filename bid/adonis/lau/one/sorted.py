#!/usr/bin/env python3
# -*- coding:utf-8 -*-


# 排序
print(sorted([36, 5, -12, 9, -21]))

# 添加排序条件
# 按照绝对值排序，但是不影响原值
print(sorted([36, 5, -12, 9, -21], key=abs))

# 排序时不区分大小写
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))

# 排序时可以添加多个条件
# 倒序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]


def by_name(t):
    return t[0]


# 按名字排序
print(sorted(L, key=by_name))


def by_score(t):
    return t[1]


# 从小到大排序
print(sorted(L, key=by_score))
# 从大到小排序
print(sorted(L, key=by_score, reverse=True))
