#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/1/30
'''
二分查找算法

二分查找也称折半查找（Binary Search），它是一种效率较高的查找方法。
但是，折半查找要求线性表必须采用顺序存储结构，而且表中元素按关键字有序排列。
'''

def binary_search(l,guess):
    min =0
    max =len(l)-1
    while min <= max:
        mid = int((min + max) / 2)
        if guess < l[mid]:
            max =mid -1
        if guess > l[mid]:
            min =mid +1
        if guess == l[mid]:
            return l[mid]

if __name__ == '__main__':
    l = [1,2,3,4,5,6]
    print(binary_search(l,4))
