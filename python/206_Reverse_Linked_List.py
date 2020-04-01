# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return None

        curr = ListNode(head.val)
        while head.next:
            head = head.next
            next_node = curr
            curr = ListNode(head.val)
            curr.next = next_node
        return head
