#
# @lc app=leetcode id=337 lang=python3
#
# [337] House Robber III
#
from typing import Optional

"""
确定子问题：
对于每一个节点 node，小偷有两种选择：
- 偷当前节点，那么就不能偷它的左右子节点。
- 不偷当前节点，那么可以偷它的左右子节点。
我们需要为每一个节点计算这两种选择下的最大金额，并使用这些值来递归地解决整个问题。

定义状态：
对于树上的每个节点 node，我们用一个长度为2的数组 dp 来表示状态：
- dp[0] 表示不偷当前节点所能获得的最大金额。
- dp[1] 表示偷当前节点所能获得的最大金额。


# 后续遍历
"""


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        result = self.dfs(root)
        return max(result[0], result[1])

    def dfs(self, node):
        if not node:
            return [0, 0]

        left = self.dfs(node.left)
        right = self.dfs(node.right)

        # 偷当前节点
        rob_res = node.val + left[0] + right[0]
        # 不偷当前节点
        not_rob = max(left[0], left[1]) + max(right[0], right[1])

        return [not_rob, rob_res]


# @lc code=end
