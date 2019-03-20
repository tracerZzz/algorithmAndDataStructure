#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Created by zzz on 2019/3/20
'''
二叉树
遍历：
    1.广度优先（层序遍历）
    2.深度优先遍历：
        2_1. 前序遍历 node——left——right
        2_2. 中序遍历 left——node——right
        2_3. 后序遍历 left——right——node
    3.树深度
    4.两棵树是否一样
'''


class TreeNode():
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 层序遍历(广度优先遍历) 循环实现
def lookup(root):
    row = [root]
    result = []
    while row:
        result += [i.data for i in row]
        row = [kid for item in row for kid in (item.left, item.right) if kid]
    print(result)


# 层序遍历(广度优先遍历) 尾递归实现
def lookup2(nodelist, result=[]):
    if len(nodelist) == 0 or not nodelist:
        print(result)
        return
    result += [i.data for i in nodelist]
    return lookup2([node for item in nodelist for node in (item.left, item.right) if node], result)


'''
深度优先遍历
前序
后序
中序
'''


# 前序遍历
def pre_traversal(root):
    if not root:
        return
    print(root.data)
    pre_traversal(root.left)
    pre_traversal(root.right)


# 后序遍历
def post_traversal(root):
    if not root:
        return
    post_traversal(root.left)
    post_traversal(root.right)
    print(root.data)


# 中序遍历
def mid_traversal(root):
    if not root:
        return
    mid_traversal(root.left)
    print(root.data)
    mid_traversal(root.right)


'''
最大树深
'''


def max_deep(root):
    if not root:
        return 0
    return max(max_deep(root.left), max_deep(root.right)) + 1


'''
判断两棵树是否相同
'''


def is_same_tree(p, q):
    if p is None and q is None:
        return True
    elif p and q:
        return p.data == q.data and is_same_tree(p.left, q.left) and is_same_tree(p.right, q.right)
    else:
        return False


if __name__ == '__main__':
    t = TreeNode(0, TreeNode(1, TreeNode(3), TreeNode(4)), TreeNode(2, TreeNode(5), TreeNode(6)))
    # lookup2([t])
    # pre_traversal(t)
    # post_traversal(t)
    # mid_traversal(t)
    print(max_deep(t))
