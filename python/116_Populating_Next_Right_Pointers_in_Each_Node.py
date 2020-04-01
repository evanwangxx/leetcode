# You are given a perfect binary tree where all leaves are on the same level,
# and every parent has two children. The binary tree has the following definition:
#
# struct Node {
#   int val;
#   Node *left;
#   Node *right;
#   Node *next;
# }
# Populate each next pointer to point to its next right node.
# If there is no next right node, the next pointer should be set to NULL.
# Initially, all next pointers are set to NULL.
#
# Follow up:
# You may only use constant extra space.
# Recursive approach is fine, you may assume implicit stack space does not count as extra space for this problem.
#
# Example 1:
#       Input: root = [1,2,3,4,5,6,7]
#       Output: [1,#,2,3,#,4,5,6,7,#]
#       Explanation: Given the above perfect binary tree (Figure A),
#               your function should populate each next pointer to point to its next right node,
#               just like in Figure B.
#                    The serialized output is in level order as connected by the next pointers,
#               with '#' signifying the end of each level.


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root):
        if not root:
            return root

        stack = [root]
        helper_stack = []
        while stack or helper_stack:
            if not stack:
                stack = helper_stack
                helper_stack = []
                continue

            node = stack.pop(0)
            node.next = stack[0] if stack else None
            # nv = node.next.val if node.next else None
            # print(node.val, nv)
            if node.left:
                helper_stack.append(node.left)
            if node.right:
                helper_stack.append(node.right)
        return root


node_2 = Node(2, Node(4, None, None), Node(5, None, None))
node_3 = Node(3, Node(6, None, None), Node(7, None, None))
test_tree = Node(1, node_2, node_3)

Solution().connect(test_tree)