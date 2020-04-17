# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        if not inorder or not postorder:
            return None

        root = TreeNode(postorder[-1])
        inorder_root_index = inorder.index(postorder[-1])

        root.left = self.buildTree(inorder[0:inorder_root_index], postorder[0:inorder_root_index])
        root.right = self.buildTree(inorder[inorder_root_index+1:], postorder[inorder_root_index:-1])
        return root
