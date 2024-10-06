#
# @lc app=leetcode id=1049 lang=python3
#
# [1049] Last Stone Weight II
#
from typing import List


# @lc code=start
class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_sum = sum(stones)

        target = stones_sum // 2

        table = [False] * (
            target + 1
        )  # 主要是因为我们需要表示从重量 0 到 target 的所有可能的子集重量。
        table[0] = True  # table[i] represents if have stones can sum to i.

        for stone in stones:
            for j in range(target, stone - 1, -1):
                table[j] = table[j] or table[j - stone]

        # 找到离 total_weight // 2 最近的 True 的索引。
        for j in range(target, -1, -1):
            if table[j]:
                return stones_sum - 2 * j

    def lastStoneWeightII(self, stones: List[int]) -> int:
        stones_nums = sum(stones)
        target = stones_nums // 2
        table = [False] * (target + 1)

        for stone in stones:
            for i in range(target, stone - 1, -1):
                table[i] = table[i] or table[i - stone]

        for j in range(target, -1, -1):
            if table[j]:
                return stones_nums - 2 * j


# @lc code=end
