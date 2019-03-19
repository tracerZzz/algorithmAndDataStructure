#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/3/19
'''
合并两个有序列表使合并好的列表依然有序

思路：创建一个临时列表，对比两个有序列表的第一个元素，将小的放入临时列表
直至其中一个列表为空，将剩下的列表追加到临时列表中，返回临时列表
'''


# 尾递归实现
def merge_sortedlist(l1, l2, tem=[]):
    if len(l1) == 0 or len(l2) == 0:
        tem = tem + l1 + l2
        return tem
    if l1[0] < l2[0]:
        tem.append(l1[0])
        del l1[0]
    else:
        tem.append(l2[0])
        del l2[0]
    return merge_sortedlist(l1, l2, tem)


# 循环实现

def merge_sortedlist2(l1, l2):
    tem =[]
    while len(l1) !=0 and len(l2) !=0:
        if l1[0] < l2[0]:
            tem.append(l1[0])
            del l1[0]
        else:
            tem.append(l2[0])
            del l2[0]
    tem.extend(l1)
    tem.extend(l2)
    return  tem


if __name__ == '__main__':
    l1 = [2, 3, 6, 7, 45, 66]
    l2 = [1, 9, 10]
    result = merge_sortedlist2(l1, l2)
    print(result)
    pass
