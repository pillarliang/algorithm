#
# @lc app=leetcode id=513 lang=python3
#
# [513] Find Bottom Left Tree Value
#
from typing import Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        self.res = None
        self.max_depth = -1
        self.helper(root, 0)
        return self.res

    def helper(self, node, depth):
        if not node:
            return
        if not node.left and not node.right:
            if depth > self.max_depth:
                self.max_depth = depth
                self.res = node.val
            return

        # 先遍历左子树，再遍历右子树
        self.helper(node.left, depth + 1)
        self.helper(node.right, depth + 1)


# @lc code=end
