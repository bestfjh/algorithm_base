#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 三十二画生JH
# @Contact : fjhstudent@163.com
# @Software: PyCharm
# @Time    : 2022/4/17 17:59
# @Site    : 网址
# @File    : linked_list.py
# @Version : 

# ---功能描述
"""
在python中实现链表，定义节点
"""
# 正文


class Node(object):
    def __init__(self, elem):
        self.elem = elem
        self.Next = None


class SingleLinkedList(object):
    """单链表"""
    """将这个类实例化时，构造函数需要做什么"""
    def __init__(self, node=None):
        self.__head = node       # 创建头节点变量，加下划线代表是私有属性

    def is_empty(self):
        return self.__head is None

    def length(self):
        """链表长度"""
        # cur是游标，或者叫指针，用来移动
        cur = self.__head
        # count记录数量
        count = 0
        while cur is not None:
            count += 1
            cur = cur.Next
        return count

    def travel(self):
        """遍历整个链表"""
        cur = self.__head
        while cur is not None:
            print(cur.Next)
            cur = cur.Next

    def add(self, item):
        pass

    def append(self, item):
        """链表尾部添加元素"""
        node = Node(item)
        if self.is_empty():
            self.__head = node
        else:
            cur = self.__head
            while cur.Next is not None:
                cur = cur.Next
            cur.Next = node

    def insert(self, pos, item):
        """ 指定位置添加元素
        :param pos:
        :param item:
        :return:
        """
        if pos <= 0:
            self.add(item)
        elif pos > (self.length()-1):
            self.append(item)
        else:
            pre = self.__head
            count = 0
            while count < (pos - 1):
                count += 1
                pre = pre.Next
            node = Node(item)
            node.next = pre.Next
            pre.next = node

    def remove(self, item):
        pass

    def search(self, item):
        pass


ll = SingleLinkedList()
print(ll.is_empty())
print(ll.length())

ll.append(1)
print(ll.is_empty())
print(ll.length())

ll.append(2)
ll.add(8)
ll.append(3)
ll.append(4)
ll.append(5)
ll.append(6)
# 8 1 2 3 4 5 6
ll.insert(-1, 9)
ll.insert(3, 100)
ll.insert(10, 200)
ll.travel()

























