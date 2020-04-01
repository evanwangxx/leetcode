# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        queue = [root]
        seq = []
        while queue:
            node = queue.pop(0)
            if not node:
                seq.append(node)
            else:
                seq.append(node.val)

            if node.left:
                queue.append(node.left)
            else:
                queue.append(None)

            if node.right:
                queue.append(node.right)
            else:
                queue.append(None)
        return seq


    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))