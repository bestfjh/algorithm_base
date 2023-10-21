#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author  : 三十二画生JH
# @Contact : fjhstudent@163.com
# @Software: PyCharm
# @Time    : 2023/10/5 15:19
# @Site    : 网址
# @File    : sumOfSquares_fjh.py
# @Version : 

# ---功能描述
"""

"""
# 正文


def sum_of_squares(nums):
    n = len(nums)
    square_all = 0
    for i, num in enumerate(nums):
        if n % (i + 1) == 0:
            square_all = square_all + num * num
    print(square_all)
    return square_all


def main():
    nums = [1, 4, 4, 7, 8, 9, 10, 11, 11, 11, 22, 22, 22]
    sum_of_squares(nums)


if __name__ == "__main__":
    main()



