# Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.
#
# For this problem, a height-balanced binary tree is defined as a binary tree
# in which the depth of the two subtrees of every node never differ by more than 1.
#
# Example:
#       Given the sorted linked list: [-10,-3,0,5,9],
#       One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:
#
#                 0
#                / \
#              -3   9
#              /   /
#            -10  5


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head):
        array = self.convert_list_to_array(head)
        return self.convert_array_to_bst(array)

    def convert_list_to_array(self, head):
        res = []
        while head:
            res.append(head.val)
            head = head.next
        return res

    def convert_array_to_bst(self, xs):
        if not xs:
            return None

        root_index = int(len(xs) / 2)
        root = TreeNode(xs[root_index])
        root.left = self.convert_array_to_bst(xs[:root_index])
        root.right = self.convert_array_to_bst(xs[root_index+1:])

        return root





