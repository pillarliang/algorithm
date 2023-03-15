class TreeNode(object):

    def __init__(self, val, left=None, right=None) -> None:
        self.val = val
        self.left = None
        self.right = None


def BST_insert(root, val):
    """二叉排序树的插入操作"""
    if (root is None):
        return TreeNode(val)
    elif root.val == val:
        # 树中存在相同关键字的结点，插入失败
        return 0
    elif root.val < val:
        root.right = BST_insert(root.right, val)
    else:
        root.left = BST_insert(root.left, val)
    return root
