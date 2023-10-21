#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 三十二画生JH
# @Contact : fjhstudent@163.com
# @Software: PyCharm
# @Time    : 2023/10/4 21:39
# @Site    : 网址
# @File    : removeDuplicate_fjh.py
# @Version : 

# ---功能描述
"""

"""
# 正文


def remove_duplicates(nums):
    n = len(nums)
    new_nums = []
    hash_table = dict()
    j = 0
    for i, num in enumerate(nums):
        if num not in hash_table:
            print(i, num)
            new_nums[j] = nums[i]
            hash_table[nums[i]] = j
            j = j + 1
    return []


def remove_duplicates_new(nums):
    index = 0
    for i, num in enumerate(nums):
        if nums[i] != nums[index]:
            index = index + 1
            nums[index] = nums[i]
    print(index+1)
    print(nums)
    return index+1


def main():
    nums = [1, 4, 4, 7, 8, 9, 10, 11, 11, 11, 22, 22, 22]
    remove_duplicates_new(nums)


if __name__ == "__main__":
    main()

