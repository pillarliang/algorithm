#
# @lc app=leetcode id=226 lang=python3
#
# [226] Invert Binary Tree
#
from typing import Optional
from collections import deque


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root

        queue = deque([root])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                cur.left, cur.right = cur.right, cur.left

                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

        return root


# @lc code=end
