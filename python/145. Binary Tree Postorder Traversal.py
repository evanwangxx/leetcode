# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root):
        res = []
        self.iterate_traversal(root, res)
        return res

    def recursion_traversal(self, node, res):
        if not node:
            return
        self.recursion_traversal(node.left, res)
        self.recursion_traversal(node.right, res)
        res.append(node.val)

    def iterate_traversal(self, node, res):
        stack = []
        while node or stack:
            if node:
                stack.append(node)
                res.insert(0, node.val)
                node = node.right
            else:
                node = stack.pop()
                node = node.left


