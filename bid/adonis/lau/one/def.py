#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x > 0:
        return x
    else:
        return -x


print(my_abs(-99))

a = abs
print(a(-88))


# 如果什么也不想坐，可以使用pass
def my_pass():
    pass


import math


# 函数返回多个值
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny


x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
print(math.pi)

r = move(100, 100, 60, math.pi / 6)
print(r)


# 计算x的n次方
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s


print(power(5, 2))
print(power(5))


# 默认参数带来的坑
def add_end(L=[]):
    L.append('END')
    return L


# 正常调用
print(add_end([1, 2, 3]))
# 非正常调用
print(add_end())
print(add_end())
print(add_end())


# Python函数在定义的时候，默认参数L的值就被计算出来了，即[]，因为默认参数L也是一个变量，它指向对象[]，
# 每次调用该函数，如果改变了L的内容，则下次调用时，默认参数的内容就变了，不再是函数定义时的[]了。
# 所以，定义默认参数要牢记一点：默认参数必须指向不变对象！

# 要修改上面的例子，我们可以用None这个不变对象来实现：
def add_end(L=None):
    if L is None:
        L = []
    L.append('END')
    return L


# 正常调用
print(add_end([1, 2, 3]))
# 非正常调用
print(add_end())
print(add_end())
print(add_end())


# 不可变参数
def cacl(number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


# 不可变参数的函数调用，多参数需要先组装list或者是tuple
print(cacl([1, 2, 3]))
print(cacl((1, 2, 3, 4)))


# 可变参数
def cacl(*number):
    sum = 0
    for n in number:
        sum = sum + n * n
    return sum


# 可变参数调用
print(cacl(1, 2, 3))
print(cacl(1, 2, 3, 4))
# 如果已经有了list或者是tuple
nums = [1, 2, 3, 4]
print(cacl(nums[0], nums[1], nums[2]))
print(cacl(*nums))


# 关键字参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 关键字参数调用
person('adonis', 22)
person('adonis', 22, city='Shanghai', job='coder')
# 如果已有dict
extra = {'city': 'city', 'job': 'job'}
person('name', '11', **extra)


# 命名关键字参数
# 如果要限制关键字参数的名字，就可以用命名关键字参数，例如，只接收city和job作为关键字参数。这种方式定义的函数如下：
def person(name, age, *, city, job):
    print(name, age, city, job)


person('adonis', 22, city='Shanghai', job='Coder')
