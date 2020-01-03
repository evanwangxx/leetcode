# Data Structure: Bisection Tree Traversal
#   1. pre-order   (recursion)
#   2. pre-order   (stack)
#   3. in-order    (recursion)
#   4. in-order    (stack)
#   5. post-order  (recursion)
#   6. level-order (stack)


class TreeNode:
    def __init__(self, node, lc, rc):
        self.node_name = node
        self.lc = lc
        self.rc = rc


class TreeTraversal:
    @staticmethod
    def pre_traversal(tree: TreeNode):
        out = [tree.node_name]
        if tree.lc:
            out_l = TreeTraversal.pre_traversal(tree.lc)
            out += out_l
        if tree.rc:
            out_r = TreeTraversal.pre_traversal(tree.rc)
            out += out_r
        return out

    @staticmethod
    def pre_traversal_stack(tree: TreeNode):
        out = []
        stack = []
        node_pointer = tree
        while node_pointer or stack:
            if node_pointer:
                stack.append(node_pointer)
                out.append(node_pointer.node_name)
                node_pointer = node_pointer.lc
            else:
                node_pointer = stack.pop(len(stack)-1)
                node_pointer = node_pointer.rc
        return out

    @staticmethod
    def in_traversal(tree: TreeNode):
        out = []
        if tree.lc:
            out_l = TreeTraversal.in_traversal(tree.lc)
            out += out_l
        out += [tree.node_name]
        if tree.rc:
            out_r = TreeTraversal.in_traversal(tree.rc)
            out += out_r
        return out

    @staticmethod
    def in_traversal_stack(tree: TreeNode):
        out = []
        stack = []
        node_pointer = tree
        while node_pointer or stack:
            if node_pointer:
                stack.append(node_pointer)
                node_pointer = node_pointer.lc
            else:
                node_pointer = stack.pop(len(stack)-1)
                out.append(node_pointer.node_name)
                node_pointer = node_pointer.rc
        return out

    @staticmethod
    def post_traversal(tree: TreeNode):
        out = []
        if tree.lc:
            out_l = TreeTraversal.post_traversal(tree.lc)
            out += out_l
        if tree.rc:
            out_r = TreeTraversal.post_traversal(tree.rc)
            out += out_r
        out += [tree.node_name]
        return out

    @staticmethod
    def level_traversal(tree: TreeNode):
        queue = [tree]
        out = []
        while queue:
            node = queue.pop(0)
            out.append(node.node_name)
            if node.lc:
                queue.append(node.lc)
            if node.rc:
                queue.append(node.rc)
        return out


if __name__ == "__main__":
    node_5 = TreeNode(5, TreeNode(7, None, None), TreeNode(8, None, None))
    node_1 = TreeNode(1, TreeNode(3, None, None), TreeNode(4, None, None))
    node_2 = TreeNode(2, node_5, TreeNode(6, None, None))
    test_tree = TreeNode(0, node_1, node_2)

    print(TreeTraversal.pre_traversal(test_tree))
    print(TreeTraversal.pre_traversal_stack(test_tree))
    print(TreeTraversal.in_traversal(test_tree))
    print(TreeTraversal.in_traversal_stack(test_tree))
    print(TreeTraversal.post_traversal(test_tree))
    print(TreeTraversal.level_traversal(test_tree))
