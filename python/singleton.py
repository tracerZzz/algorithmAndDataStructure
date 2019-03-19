#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/3/19

'''
单例模式
1.__new_
2.共享属性
3.装饰器
4.模块引入
5.元类
'''

'''
__new__
'''


class Singleton():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instance


class A(Singleton):
    age = 1


'''
共享属性
'''


class Brog():
    _state = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Brog, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._state
        return obj


class B(Brog):
    age = 1


'''
元类
'''


class SingleMateClass(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(SingleMateClass, cls).__call__(*args, **kwargs)
        return cls._instances[cls]


class C(metaclass=SingleMateClass):
    age = 1


'''
装饰器
装饰器的作用就是将函数或类进行一次包装，返回一个新的函数或者新的类

执行D()之前先执行了装饰器，由于是类装饰器，需要先创建一个装饰器的对象，进行初始化
将类D传给初始化函数，再调用__call__方法，返回一个单例模式
'''


# 类装饰器
class DecoratorClass():
    _instances = {}

    def __init__(self, cls):
        self._cls = cls

    def __call__(self, *args, **kwargs):
        if self._cls not in self._instances:
            obj = self._cls(*args, **kwargs)
            self._instances[self._cls] = obj
        return self._instances[self._cls]


@DecoratorClass
class D:
    age = 1
    def __init__(self,age):
        self.age=age


# 函数装饰器
# 同时这也是一个闭包
def FuncDecorator(cls):
    _instances = {}
    def get_instance(*args, **kwargs):
        if cls not in _instances:
            obj = cls(*args, **kwargs)
            _instances[cls] = obj
        return _instances[cls]

    return get_instance


# 装饰器作用在类上和作用在__new__上，效果是一样的，但当在类上使用装饰器同时定义__new__方法时，在调用super时，会因为装饰器改变了类型而报错
# 所以尽量不让__new__ 和装饰器通时出现
@FuncDecorator
class E:
    age = 1

    # @FuncDecorator
    # def __new__(cls, *args, **kwargs):
    #     return super(E, cls).__new__(cls, *args, **kwargs)


if __name__ == '__main__':
    a = D(2)
    b = D(3)
    print(id(a) == id(b))
    print(a.age)
    a.age += 2
    print(b.age)

    pass
