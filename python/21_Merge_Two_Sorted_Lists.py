# Merge two sorted linked lists and return it as a new list.
# The new list should be made by splicing together the nodes of the first two lists.
#
# Example:
#   Input: 1->2->4, 1->3->4
#   Output: 1->1->2->3->4->4

# Definition for singly-linked list.

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1:
            return l2
        if not l2:
            return l1

        if l1.val <= l2.val:
            result = ListNode(l1.val)
            result.next = self.mergeTwoLists(l1.next, l2)
            return result
        else:
            result = ListNode(l2.val)
            result.next = self.mergeTwoLists(l1, l2.next)
            return result

    def show(self, x: ListNode):
        print(x.val)
        if x.next:
            self.show(x.next)


if __name__ == "__main__":
    n1_1 = ListNode(1)
    n1_2 = ListNode(2)
    n1_4 = ListNode(4)
    n2_1 = ListNode(1)
    n2_3 = ListNode(3)
    n2_4 = ListNode(4)

    n1_2.next = n1_4
    n1_1.next = n1_2
    n2_3.next = n2_4
    n2_1.next = n2_3

    s = Solution()
    result = s.mergeTwoLists(n1_1, n2_1)
    print(s.show(result))



