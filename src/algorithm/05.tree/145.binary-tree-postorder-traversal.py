#
# @lc app=leetcode id=145 lang=python3
#
# [145] Binary Tree Postorder Traversal
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
    """using recursive traversal"""
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []

        return self.postorderTraversal(root.left) + self.postorderTraversal(
            root.right) + [root.val]


# @lc code=end


class Solution2:
    """using recursive traversal"""
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        stack = []
        cur = root
        rec = None

        while cur or stack:
            if cur:
                stack.append(cur)
                cur = cur.left
            else:
                cur = stack[-1]
                if cur.right and rec != cur.right:
                    cur = cur.right
                else:
                    cur = stack.pop()
                    result.append(cur.val)
                    rec = cur
                    cur = None
        return result
