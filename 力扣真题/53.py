#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 三十二画生JH
# @Contact : fjhstudent@163.com
# @Software: PyCharm
# @Time    : 2023/6/18 13:40
# @Site    : 网址
# @File    : 53.py
# @Version : 

# ---功能描述
"""

"""
# 正文

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        sum = 0
        max = nums[0]
        for i in range(n):
            for j in range(i+1, n):
                for k in range(i, j+1):
                    sum = sum + nums[k]
                if sum >= max:
                    max = sum
                sum = 0
        return max





