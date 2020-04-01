# Given a linked list, remove the n-th node from the end of list and return its head.
# Example:
#       Given linked list: 1->2->3->4->5, and n = 2.
#       After removing the second node from the end, the linked list becomes 1->2->3->5.
# Note: Given n will always be valid.
# Follow up: Could you do this in one pass?


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if n == 0:
            return head

        f = head
        for i in range(0, n):
            if f.next:
                f = f.next
            else:
                return head.next
        s = head
        while f.next:
            f = f.next
            s = s.next
        s.next = s.next.next
        return head

    def show(self, x: ListNode):
        if x:
            print(x.val)
            if x.next:
                self.show(x.next)


if __name__ == "__main__":
    n1 = ListNode(1)
    n2 = ListNode(2)
    n3 = ListNode(3)
    n4 = ListNode(4)
    n5 = ListNode(5)

    n4.next = n5
    n3.next = n4
    n2.next = n3
    n1.next = n2

    s = Solution()
    r = s.removeNthFromEnd(n1, 2)
    s.show(r)

    m1 = ListNode(1)
    s = Solution()
    r = s.removeNthFromEnd(m1, 1)
    s.show(r)
