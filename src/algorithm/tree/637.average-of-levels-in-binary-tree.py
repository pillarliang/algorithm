#
# @lc app=leetcode id=637 lang=python3
#
# [637] Average of Levels in Binary Tree
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


"""
Solution() takes up more memory than Solition1()
"""


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return 0

        queue = deque([root])
        while queue:
            sub_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                sub_res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            result.append(round(sum(sub_res) / len(sub_res), 5))

        return result


# @lc code=end
class Solution1:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        result = []
        if not root:
            return 0

        queue = deque([root])
        while queue:
            # sum directly
            sub_res_sum = 0
            size = len(queue)
            for _ in range(size):
                cur = queue.popleft()
                sub_res_sum += cur.val
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            result.append(round(sub_res_sum / size, 5))

        return result
