# Given a singly linked list L: L0→L1→…→Ln-1→Ln,
# reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…
#
# You may not modify the values in the list's nodes, only nodes itself may be changed.
#
# Example 1:
#       Given 1->2->3->4, reorder it to 1->4->2->3.
# Example 2:
#       Given 1->2->3->4->5, reorder it to 1->5->2->4->3.


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return
        self.dict_reorder(head)

    def dict_reorder(self, head):
        i = 0
        dic = {}
        while head:
            dic[i] = head
            i += 1
            head = head.next

        start = 0
        tail = len(dic) - 1
        while start < tail:
            dic[start].next, dic[tail].next = dic[tail], dic[start].next
            start += 1
            tail -= 1
        dic[start].next = None
        return dic[0]

node4 = ListNode(4)
node3 = ListNode(3)
node2 = ListNode(2)
node1 = ListNode(1)

node1.next = node2
node2.next = node3
node3.next = node4

res = Solution().reorderList(node1)
i = 1
while res and i < 10:
    print(res.val)
    res = res.next
    i += 1
