#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/1/29


'''
台阶问题/斐波那契

一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法。
'''

fib = lambda n: n if n <= 2 else fib(n - 1) + fib(n - 2)


'''
一个台阶总共有n级，如果一次可以跳1级，也可以跳2级...它也可以跳上n级。此时该青蛙跳上一个n级的台阶总共有多少种跳法？
Fib(n) = Fib(n-1)+Fib(n-2)+Fib(n-3)+..........+Fib(n-n)
Fib(n) = Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-1)
Fib(n-1) =  Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-1)+Fib(n-2)
做减法
Fib(n)-Fib(n-1)=-Fib(n-2)
Fib(n-1)=Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-1)+Fib(n-2)
Fib(n)=-Fib(n-2) +Fib(0)+Fib(1)+Fib(2)+.......+Fib(n-1)+Fib(n-2)
Fib(n)=2Fib(n-1)

'''
fib2 = lambda n: n if n ==1 else 2*fib2(n-1)

if __name__ == '__main__':
    print(fib(4))
    print(fib2(3))
    pass
