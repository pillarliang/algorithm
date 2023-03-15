class TreeNode(object):

    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right


class RecursiveTraversal(object):
    """二叉树的递归遍历"""

    def pre_order(self, root):
        """前序遍历"""
        if root is None:
            return []
        return [root.value] + self.pre_order(root.left) + self.pre_order(
            root.right)

    def in_order(self, root):
        """中序遍历"""
        if root is None:
            return []
        return self.pre_order(root.left) + [root.value] + self.pre_order(
            root.right)

    def pos_order(self, root):
        """后序遍历"""
        if root is None:
            return []
        return self.pre_order(root.left) + self.pre_order(
            root.right) + [root.value]
