#
# @lc app=leetcode id=257 lang=python3
#
# [257] Binary Tree Paths
#
from typing import Optional, List


# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        solutions = []  # 存储所有从根到叶子的路径
        state = ""
        if not root:
            return solutions
        self.search(root, state, solutions)  # 从根节点开始回溯搜索
        return solutions

    def search(self, node, state, solutions):
        if not node:
            return

        state += str(node.val)  # 将当前节点的值添加到当前路径
        # 检查当前节点是否是叶子节点 => 相当于 is_valid_state(): 一条有效的路径就是当前节点是叶子节点的状态。
        if not node.left and not node.right:
            # 如果是叶子节点，将路径添加到结果列表
            solutions.append(state)
            return

        # 相当于：get_candidates() 在树的结构中，左子节点和右子节点是下一个可能的状态
        # 如果不是叶子节点，继续探索左子树和右子树
        state += "->"
        self.search(node.left, state, solutions)  # 递归搜索左子树
        self.search(node.right, state, solutions)  # 递归搜索右子树


# 示例用法：
# 构建二叉树
#      1
#     / \
#    2   3
#     \
#      5
# root = TreeNode(1)
# root.left = TreeNode(2)
# root.right = TreeNode(3)
# root.left.left = TreeNode(4)
# root.left.right = TreeNode(5)
# print(solve(root))  # 输出所有从根节点到叶子节点的路径

# @lc code=end
