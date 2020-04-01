# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order and each of their nodes contain a single digit.
# Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
#
# Example:
#   Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
#   Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            l1 = ListNode(0)
        if not l2:
            l2 = ListNode(0)

        this_val = l1.val + l2.val

        if this_val >= 10:
            this_val = this_val % 10
            if l1.next:
                l1.next.val += 1
            elif l2.next:
                l2.next.val += 1
            else:
                l1.next = ListNode(1)

        this_node = ListNode(this_val)

        if l1.next or l2.next:
            this_node.next = self.addTwoNumbers(l1.next, l2.next)

        return this_node

if __name__ == "__main__":
    # test1
    x1_2 = ListNode(2)
    x1_4 = ListNode(4)
    x1_3 = ListNode(3)
    x1_4.next = x1_3
    x1_2.next = x1_4

    x2_5 = ListNode(5)
    x2_6 = ListNode(6)
    x2_4 = ListNode(4)
    x2_6.next = x2_4
    x2_5.next = x2_6

    print(Solution().addTwoNumbers(x1_2, x2_5).val)

    # test2
    y5_a = ListNode(5)
    y5_b = ListNode(5)

    print(Solution().addTwoNumbers(y5_a, y5_b).val)

