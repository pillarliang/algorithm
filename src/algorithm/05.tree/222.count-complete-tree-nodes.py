#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
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
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return self.countNodes(root.right) + self.countNodes(root.left) + 1
# @lc code=end

