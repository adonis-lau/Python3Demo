#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# This is My First Python Program

classmates = ['Michael', 'Bob', 'Tracy']

print(classmates)

print(len(classmates))

print(classmates[0])

# print(classmates[3])   #list中只有三个元素，下标从0-2，获取下表为3的元素，会报错：IndexError : list index out of range

print(classmates[-1])  # 下标使用-1，可以获取list中最后一个元素

classmates.append('Adonis')
print(classmates)  # 添加元素到list末尾

classmates.insert(1, 'Lau')  # 将元素插入到指定位置，下标从0开始
print(classmates)

classmates.pop(-1)  # 删除指定下标的元素，下标从0开始
print(classmates)
