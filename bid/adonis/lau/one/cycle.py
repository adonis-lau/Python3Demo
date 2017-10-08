#!/usr/bin/env python3
# -*- conding: utf-8 -*-

names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

peoples = ('Michael', 'Bob', 'Tracy')
for people in peoples:
    print(people)

# range(x)   代表从0到x的所有数值
print(list(range(10)))
sum = 0
for x in range(10):
    sum += x
print(sum)

sum = 0
n = 99
while n > 0:
    sum += n
    print(n)
    n -= 2
print(sum)

# break continue 关键字与其他语言相同