#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/1/29


'''
台阶问题

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)



'''
矩形覆盖问题

我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。
请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

fib2(n - 1) + fib2(n - 2)可以理解为第一步跳一个台阶的所有可能性+第一步跳两部的所有可能性
'''

fib2 = lambda n: n if n == 1 else fib2(n - 1) + fib2(n - 2)




'''
台阶问题拓展

一个台阶总共有n级，如果一次可以跳1级，也可以跳2级...它也可以跳上n级。
此时该青蛙跳上一个n级的台阶总共有多少种跳法？
Fib(n) = Fib(n-1)+Fib(n-2)+Fib(n-3)+..........+Fib(n-n)
可以理解为第一步跳一个台阶的所有可能性+第一步跳两部的所有可能性+....+一步跳完的可能性

Fib(n) = Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-1)
Fib(n-1) =  Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-3)+Fib(n-2)
做减法
Fib(n)-Fib(n-1)=Fib(n-1)
Fib(n)=2Fib(n-1)

'''
fib3 = lambda n: n if n == 1 else 2 * fib3(n - 1)

if __name__ == '__main__':
    pass
