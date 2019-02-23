#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 19-2-22

'''
快排

基本思想：选择一个基准元素,通常选择第一个元素或者最后一个元素,通过一趟扫描，
将待排序列分成两部分,一部分比基准元素小,一部分大于等于基准元素,
此时基准元素在其排好序后的正确位置,然后再用同样的方法递归地排序划分的两部分
'''

'''
递归实现
'''
def quick_sort(list):
    if len(list) < 2:
        return list
    mid = list[0]
    less_list = [i for i in list[1:] if i < mid]
    bigger_list = [i for i in list[1:] if i >= mid]
    finnal_list = quick_sort(less_list) + [mid] + quick_sort(bigger_list)
    return finnal_list


if __name__ == '__main__':
    print(quick_sort([2]))
    print(quick_sort([332,32,34,55,56,1,4]))
    pass
