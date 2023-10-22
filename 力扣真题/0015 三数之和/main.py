# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Solution:
    def threeSum(self, nums):
        nums.sort()
        record = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l = i + 1
            r = len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    record.append([nums[i], nums[l], nums[r]])
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r-1] == nums[r]:
                        r -= 1
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                else:
                    l += 1
        return record


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    fu1 = Solution()
    print(fu1.threeSum([-1, 0, 1, 2, -1, -4]))


# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# class Solution:
#     def threeSum(self, nums: List[int]) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()  # 对 nums 数组进行升序排序
#         res = []  # 定义一个控制的列表（数组）
#
#         for i in range(n - 2):
#             if i > 0 and nums[i] == nums[i - 1]:
#                 continue
#             l = i + 1
#             r = n - 1
#             while (l < r):
#                 if (nums[i] + nums[l] + nums[r] < 0):
#                     l += 1
#                 elif (nums[i] + nums[l] + nums[r] > 0):
#                     r -= 1
#                 else:
#                     res.append([nums[i], nums[l], nums[r]])
#                     while (l < r and nums[l] == nums[l + 1]):
#                         l += 1
#                     while (l < r and nums[r] == nums[r - 1]):
#                         r -= 1
#                     l += 1
#                     r -= 1
#         return res













