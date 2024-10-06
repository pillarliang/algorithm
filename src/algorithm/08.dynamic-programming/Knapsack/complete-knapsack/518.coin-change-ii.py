#
# @lc app=leetcode id=518 lang=python3
#
# [518] Coin Change II
#
from typing import List


# @lc code=start
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        table = [0] * (amount + 1)  # 初始化 dp 数组，长度为 amount + 1
        table[0] = 1  # 凑成金额 0 的组合数为 1（即不选任何硬币）

        # 遍历每个硬币
        for coin in coins:
            # 从 coin 到 amount 更新 dp 数组
            for j in range(coin, amount + 1):
                table[j] += table[j - coin]

        return table[amount]

    def change_2d(self, amount: int, coins: List[int]) -> int:
        table = [[0] * (amount + 1) for _ in range(len(coins) + 1)]

        for i in range(len(coins) + 1):
            table[i][0] = 1

        for i in range(1, len(coins) + 1):
            for j in range(amount + 1):
                # 不使用当前硬币
                table[i][j] = table[i - 1][j]
                # 使用当前硬币
                if j >= coins[i - 1]:
                    table[i][j] += table[i][j - coins[i - 1]]

        return table[len(coins)][amount]


# @lc code=end
