#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/1/30
'''
杨氏矩阵查找

在一个m行n列二维数组中，每一行都按照从左到右递增的顺序排序，
每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

使用Step-wise线性搜索。
'''


def getValue(l, value):
    m = len(l) - 1
    n = len(l[0]) - 1
    r = 0
    c = n
    while c >= 0 and r <= m:
        v = l[r][c]
        if value == v:
            return True
        elif value > v:
            r += 1
        elif value < v:
            c -= 1
    return False


if __name__ == '__main__':
    l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(getValue(l, 10))
    print(getValue(l, 7))
    pass
