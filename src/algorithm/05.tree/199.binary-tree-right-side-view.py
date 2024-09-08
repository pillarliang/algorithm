#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        queue = deque([root])

        while queue:
            sub_res = []

            # get values from a same level
            for _ in range(len(queue)):
                cur = queue.popleft()
                sub_res.append(cur.val)
                if cur.left:
                    queue.append(cur.left)
                if cur.right:
                    queue.append(cur.right)

            # after one level
            result.append(sub_res.pop())

        return result


# @lc code=end
