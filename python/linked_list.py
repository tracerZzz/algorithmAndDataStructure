#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/2/21
'''
链表
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
    list_node.next.next =list_node
    list_node.next = None
    return result



def print_list_node(listNode):
    result = ""
    while listNode is not None:
        result = result + " " + str(listNode.value)
        listNode = listNode.next
    print(result)


if __name__ == '__main__':
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6, ListNode(7)))))))
    print_list_node(l)
    result = swap_double(l)
    print_list_node(result)
    reverse_result = reverse_list(result)
    print_list_node(reverse_result)
