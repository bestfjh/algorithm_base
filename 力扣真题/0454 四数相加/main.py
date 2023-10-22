# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class Solution:
    def foursum(self, nums1, nums2, nums3, nums4):
        record = dict()
        for i1, n1 in enumerate(nums1):
            for i2, n2 in enumerate(nums2):
                if n1 + n2 in record:
                    record[n1 + n2] += 1
                else:
                    record[n1 + n2] = 1
        count = 0
        for i3, n3 in enumerate(nums3):
            for i4, n4 in enumerate(nums4):
                if -(n3+n4) in record:
                    count += record[-(n3+n4)]
        return count


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    fu1 = Solution()
    nums1 = [3, 1, 4]
    nums2 = [-2, 4, 3]
    nums3 = [-1, 3, 2]
    nums4 = [3, -2, 0]
    print(fu1.foursum(nums1, nums2, nums3, nums4))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/






