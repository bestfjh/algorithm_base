#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 三十二画生JH
# @Contact : fjhstudent@163.com
# @Software: PyCharm
# @Time    : 2023/10/5 16:42
# @Site    : 网址
# @File    : buildArray_fjh.py
# @Version : 

# ---功能描述
"""

"""
# 正文


def build_array(nums):
    for i, num in enumerate(nums):
        print(nums[nums[i]])
        return nums[nums[i]]


def build_array_new(nums):
    return [nums[nums[i]] for i in range(len(nums))]


def main():
    nums = [0, 2, 1, 5, 3, 4]

    build_array(nums)
    build_array_new(nums)


if __name__ == "__main__":
    main()

