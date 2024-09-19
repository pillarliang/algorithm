#
# @lc app=leetcode id=111 lang=python3
#
# [111] Minimum Depth of Binary Tree
#
"""
关于根节点的深度究竟是1 还是 0，不同的地方有不一样的标准，leetcode的题目中都是根节点深度是1。但维基百科上定义根节点的深度是0.
The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and root.right:
            return self.minDepth(root.right) + 1
        if not root.right and root.left:
            return self.minDepth(root.left) + 1
        
        return min(self.minDepth(root.left), self.minDepth(root.right)) + 1
# @lc code=end
