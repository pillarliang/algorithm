#
# @lc app=leetcode id=110 lang=python3
#
# [110] Balanced Binary Tree
#
"""
树的深度与高度计算时中，leetcode 中都是以节点为 1 度，但 Wikipedia 中是以边为 1 度。
返回以该节点为根节点的二叉树的高度，如果不是平衡二叉树了则返回-1
"""
from typing import Optional


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        return self.get_height(root) != -1

    def get_height(self, node):
        if not node:
            return 0
        left_height = self.get_height(node.left)
        right_height = self.get_height(node.right)
        if (
            left_height == -1
            or right_height == -1
            or abs(left_height - right_height) > 1
        ):
            return -1
        return max(left_height, right_height) + 1


# @lc code=end
