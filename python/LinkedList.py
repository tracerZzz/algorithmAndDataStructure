#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/2/21
'''
链表成对调换

1->2->3->4转换成2->1->4->3.
'''


class ListNode:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next


def swapDouble(listNode):
    if listNode.next is None:
        return listNode
    if listNode is not None and listNode.next is not None:
        next = listNode.next
        listNode.next = swapDouble(next.next)
        next.next = listNode
        return next


if __name__ == '__main__':
    l = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5, ListNode(6,ListNode(7)))))))
    result = swapDouble(l)
    while result is not None:
        print(result.head)
        result = result.next
    pass
