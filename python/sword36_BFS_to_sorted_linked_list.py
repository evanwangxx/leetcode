"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""


class Solution:
    def __init__(self):
        self.pre = None
        self.head = None
        self.tail = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if not root:
            return None

        self.tree_traversal(root)
        self.head.left = self.tail
        self.tail.right = self.head

        return self.head

    def tree_traversal(self, node):
        if not node:
            return None

        # process left
        self.tree_traversal(node.left)

        # inorder traversal, set head, tail and pointer
        if not self.pre:
            self.head = node
        else:
            self.pre.right = node

        node.left = self.pre
        self.tail = self.pre = node

        # process right
        self.tree_traversal(node.right)