# Given a binary search tree and a node in it, find the in-order successor of that node in the BST.
# The successor of a node p is the node with the smallest key greater than p.val.


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root, p):
        if not root or not p:
            return None

        if root.val <= p.val:
            return self.inorderSuccessor(root.right, p)

        res = self.inorderSuccessor(root.left, p)
        if res and res.val < root.val:
            return res
        else:
            return root
