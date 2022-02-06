#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def power(x):
    return x*x

# 当函数有多个参数时，把变化大的参数放前面，变化小的参数放后面。
# 变化小的参数可以作为默认参数。
def power(x,n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

def enroll(name, gender, age=6, city='Beijing'):
    print('Personal Info')
    print('---------------')
    print('   Name: %s' % name)
    print(' Gender: %s' % gender)
    print('   City: %s' % city)
    print('    Age: %s' % age)
    print()


# 函数的参数改为可变参数
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)


# 检查是否有city和job参数
def person(name, age, **kw):
    if 'city' in kw:
        # 有city参数
        pass
    if 'job' in kw:
        # 有job参数
        pass
    print('name:', name, 'age:', age, 'other:', kw)


def person1(name, age, *, city, job):
    print(name, age, city, job)

def person2(name, age, *args, city, job):
    print(name, age, args, city, job)

def person3(name, age, *, city='Beijing', job):
    print(name, age, city, job)    


def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)


n = power(5)
print(n)

n = power(5,4)
print(n)

enroll('Sarah', 'F')
enroll('Adam', 'M', city='Tianjin')

n1 = calc(1, 2, 3)
n2 = calc(1, 2, 3, 5, 7)
print(n1)
print(n2)

nums = [1, 2, 3]
# *nums表示把nums这个list的所有元素作为可变参数传进去
n3 = calc(*nums)
print(n3)

person('Michael', 30)
person('Bob', 35, city='Beijing')

extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Jack', 24, city=extra['city'], job=extra['job'])
person('Jack', 24, **extra)


person('Jack', 24, city='Beijing', addr='Chaoyang', zipcode=123456)


