"""二叉排序树的查找：LC700:https://leetcode.cn/problems/search-in-a-binary-search-tree/submissions/
"""


def search_bst(root, val):
    """非递归"""
    while root:
        if val < root.val:
            root = root.left
        elif val > root.val:
            root = root.right
        else:
            return root
    return None


def search_bst_recursive(root, val):
    """递归"""
    if root is None or root.val == val:
        return root
    if root.val < val:
        return search_bst_recursive(root.right, val)
    if root.val > val:
        return search_bst_recursive(root.left, val)
