#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 三十二画生JH
# @Contact : fjhstudent@163.com
# @Software: PyCharm
# @Time    : 2023/10/4 19:19
# @Site    : 网址
# @File    : TwoSum.py
# @Version : 

# ---功能描述
"""

"""
# 正文


def two_sum(nums, target):
    n = len(nums)
    print("the len of nums is: " + str(n))
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                print([i, j])
                return [i, j]
    return []


def two_num_hash(nums, target):
    hash_table = dict()
    for i, num in enumerate(nums):
        # print('nop')
        if target - num in hash_table:
            print([hash_table[target - num], i])
            return [hash_table[target - num], i]
        hash_table[nums[i]] = i
        print(hash_table)
    return []


def main():
    nums = [1, 4, 7, 8, 9, 10, 11, 43, 23, 54]
    target = 9
    two_sum(nums, target)
    two_num_hash(nums, target)


if __name__ == "__main__":
    main()
