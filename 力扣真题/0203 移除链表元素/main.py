# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


class ListNode:
    def __init__(self, val=0, next = None):
        self.val = val
        self.next = next


class Solution:
    def removeElements(self, head, val):
        self.fu = ListNode(next = head)

        dummy_head = ListNode(next = head)
        cur = dummy_head
        while(cur.next != None):
            if (cur.next.val == val):
                cur.next = cur.next.next
            else:
                cur = cur.next
        return dummy_head.next


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    head = [1, 2, 6, 3, 4, 5, 6]
    val = 6

    fu1 = Solution()
    print(fu1.removeElements(head, val))








# See PyCharm help at https://www.jetbrains.com/help/pycharm/
