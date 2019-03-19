#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/2/21
'''
链表
1.链表成对调换
2.链表反转
3.链表求焦点
'''


class ListNode:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


'''
链表成对调换

1->2->3->4转换成2->1->4->3.
'''


def swap_double(list_node):
    if list_node.next is None:
        return list_node
    if list_node is not None and list_node.next is not None:
        next = list_node.next
        list_node.next = swap_double(next.next)
        next.next = list_node
        return next


'''
链表反转
'''


def reverse_list(list_node):
    if list_node is None or list_node.next is None:
        return list_node
    result = reverse_list(list_node.next)
    list_node.next.next = list_node
    list_node.next = None
    return result


def print_list_node(listNode):
    result = ""
    while listNode is not None:
        result = result + " " + str(listNode.value)
        listNode = listNode.next
    print(result)


'''
链表求焦点
尾部对齐，从短链表的第一个开始比较
'''


def find_same_node(l1, l2):
    if l1 is None or l2 is None:
        return
    length1, length2 = 0, 0
    tem1 = l1
    tem2 = l2
    # 求出两个链表的长度
    while tem1.next:
        length1 += 1
        tem1 = tem1.next
    while tem2.next:
        length2 += 1
        tem2 = tem2.next
    # 将两个链表尾对齐，从短的链表开始比较
    if length1 > length2:
        for _ in range(length1 - length2):
            l1 = l1.next
    elif length2 > length1:
        for _ in range(length2 - length1):
            l2 = l2.next
    # 比较
    while l1 != l2:
        l1 = l1.next
        l2 = l2.next
        # 如果到了尾部 返回，说明没有重复
        if l1 is None or l2 is None:
            return
    return l1


if __name__ == '__main__':
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    l1 = ListNode(22, ListNode(43, l))
    l2 = ListNode(33, l)
    print(find_same_node(l1, l2).value)
    # print(l1.next == l2.next)
    print_list_node(l)
    result = swap_double(l)
    print_list_node(result)
    reverse_result = reverse_list(result)
    print_list_node(reverse_result)
