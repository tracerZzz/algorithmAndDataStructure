#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 19-2-22

'''
冒泡排序
'''


def bubble(list):
    # i 代表一共要循环的次数
    for i in range(len(list) - 1):
        # j代表每个元素要比较的次数，每冒泡一次，比较的次数要减少一次
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]

    return list


if __name__ == '__main__':
    l = [0, 1, 5, 7, 87, 34, 3]
    print(bubble(l))
    pass
