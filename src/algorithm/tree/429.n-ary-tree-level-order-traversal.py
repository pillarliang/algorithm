#
# @lc app=leetcode id=429 lang=python3
#
# [429] N-ary Tree Level Order Traversal
#
from typing import List
from collections import deque

# @lc code=start


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        result = []
        if not root:
            return result

        queue = deque([root])
        while queue:
            sub_res = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                sub_res.append(cur.val)
                if cur.children:
                    for child in cur.children:
                        queue.append(child)
            result.append(sub_res)

        return result


# @lc code=end
