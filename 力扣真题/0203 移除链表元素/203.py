#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 三十二画生JH
# @Contact : fjhstudent@163.com
# @Software: PyCharm
# @Time    : 2022/4/17 14:33
# @Site    : 网址
# @File    : 203.py
# @Version : 

# ---功能描述
"""

"""
# 正文


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        dummy_head = ListNode(next=head)
        print(dummy_head.val)
        print(dummy_head.next)
        cur = dummy_head
        print(cur.next)
        print(cur.next.val)
        while(cur.next!= None):
            if (cur.next.val == val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next


head = [1]
val = 6
Remove_fu = Solution()
Remove_fu.removeElements(head, val)



