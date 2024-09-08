#
# @lc app=leetcode id=107 lang=python3
#
# [107] Binary Tree Level Order Traversal II
#
from typing import List, Optional
from collections import deque


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque([])
        queue.append(root)

        while queue:
            sub_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                sub_res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)
            result.append(sub_res)
        return result[::-1]


# @lc code=end
