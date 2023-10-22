# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Solution:
    def fourSum(self, nums, target):
        hashmap = dict()
        for n in nums:
            if n in hashmap:
                hashmap[n] += 1
            else:
                hashmap[n] = 1

        ans = set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1, len(nums)):
                    val = target - (nums[i] + nums[j] + nums[k])
                    if val in hashmap:
                        count = (nums[i] == val) + (nums[j] == val) + (nums[i] == val)
                        if hashmap[val] > count:
                            ans.add(tuple(sorted([nums[i], nums[j], nums[k], val])))
                    else:
                        continue
        return ans


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    fu1 = Solution()
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(fu1.fourSum(nums, target))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         nums.sort()
#         results = []
#         self.findNsum(nums, target, 4, [], results)
#         return results
#
#     def findNsum(self, nums, target, N, tempList, results):
#         if len(nums) < N or N < 2:
#             return
#
#         if N == 2:
#             l = 0
#             r = len(nums) - 1
#             while l < r:
#                 if nums[l] + nums[r] == target:
#                     results.append(tempList + [nums[l], nums[r]])
#                     l += 1
#                     r -= 1
#
#                     while l < r and nums[l] == nums[l - 1]:
#                         l += 1
#                     while r > 1 and nums[r] == nums[r + 1]:
#                         r -= 1
#                 elif nums[l] + nums[r] < target:
#                     l += 1
#                 else:
#                     r -= 1
#         else:
#             for i in range(0, len(nums)):
#                 if i == 0 or i > 0 and nums[i - 1] != nums[i]:
#                     self.findNsum(nums[i + 1:], target - nums[i], N - 1, tempList + [nums[i]], results)
#         return
#
#
#


class Solution1:
    def fourSum1(self, nums, target):
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]: continue
            for k in range(i + 1, n):
                if k > i + 1 and nums[k] == nums[k - 1]: continue
                p = k + 1
                q = n - 1

                while p < q:
                    if nums[i] + nums[k] + nums[p] + nums[q] > target:
                        q -= 1
                    elif nums[i] + nums[k] + nums[p] + nums[q] < target:
                        p += 1
                    else:
                        res.append([nums[i], nums[k], nums[p], nums[q]])
                        while p < q and nums[p] == nums[p + 1]: p += 1
                        while p < q and nums[q] == nums[q - 1]: q -= 1
                        p += 1
                        q -= 1
        return res

