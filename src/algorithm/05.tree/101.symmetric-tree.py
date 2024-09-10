#
# @lc app=leetcode id=101 lang=python3
#
# [101] Symmetric Tree
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

    def isSymmetric_old(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        queue = deque([root.left, root.right])

        while queue:
            if len(queue) % 2 != 0:
                return False

            level_vals = []
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur:
                    level_vals.append(cur.val)
                    queue.append(cur.left)
                    queue.append(cur.right)
                else:
                    level_vals.append(None)

            if level_vals != level_vals[::-1]:
                return False

        return True

    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        def isMirror(left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
            # 如果两个节点同时为 None，返回 True；如果只有一个为 None，返回 False
            if not left and not right:
                return True
            if not left or not right:
                return False

            # 检查当前节点值并递归检查子树
            return (
                (left.val == right.val)
                and isMirror(left.left, right.right)
                and isMirror(left.right, right.left)
            )

        return isMirror(root.left, root.right)


# @lc code=end

n_4 = TreeNode(4)
n_3 = TreeNode(3)
n_2_l = TreeNode(2, n_3, n_4)
n_2_r = TreeNode(2, n_4, n_3)
n_1 = TreeNode(1, n_2_l, n_2_r)

print(Solution().isSymmetric(n_1))
