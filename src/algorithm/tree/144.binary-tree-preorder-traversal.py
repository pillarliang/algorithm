#
# @lc app=leetcode id=144 lang=python3
#
# [144] Binary Tree Preorder Traversal
#
from typing import List, Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    """using Recursive traversal"""
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return
        return [root.val] + self.preorderTraversal(
            root.left) + self.preorderTraversal(root.right)


# @lc code=end


class Solution2:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        """using non-recursive traveral -- stack"""
        result = []
        stack = []
        cur = root
        while cur or stack:
            if cur:
                result.append(cur.val)
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack.pop()
                cur = cur.right
        return result
