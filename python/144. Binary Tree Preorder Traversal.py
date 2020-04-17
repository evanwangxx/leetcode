# Given a binary tree, return the preorder traversal of its nodes' values.
#
# Example:
#       Input: [1,null,2,3]
#                1
#                 \
#                  2
#                 /
#                3
#       Output: [1,2,3]
# Follow up: Recursive solution is trivial, could you do it iteratively?


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root):
        res = []
        self.iterate_traversal(root, res)
        return res

    def recursion_traversal(self, node, res):
        if not node:
            return

        res.append(node.val)
        if node.left:
            self.recursion_traversal(node.left, res)
        if node.right:
            self.recursion_traversal(node.right, res)

    def iterate_traversal(self, node, res):
        stack = []
        while node or stack:
            if node:
                res.append(node.val)
                stack.append(node)
                node = node.left
            else:
                node = stack.pop(len(stack)-1)
                node = node.right






