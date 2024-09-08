#
# @lc app=leetcode id=714 lang=python3
#
# [714] Best Time to Buy and Sell Stock with Transaction Fee
#
from typing import List


# @lc code=start
class Solution:
    # def maxProfit(self, prices: List[int], fee: int) -> int:
    #     """The transaction fee is only charged once for each stock purchase and sale.
    #     所以在股票卖出时支付。
    #     """
    #     # 1. 初始化
    #     n = len(prices)
    #     hold = [0] * n  # 表示在第 i 天持有股票的最大利润。
    #     cash = [0] * n  # 表示在第 i 天不持有股票的最大利润。

    #     hold[0] = -prices[0]  # 第一天买入股票
    #     cash[0] = 0  # 第一天不持有股票

    #     # 2. 填充表格 - 确定状态转移方程
    #     for i in range(1, n):
    #         # 如果我们在第 i 天持有股票，可能是因为我们在第 i-1 天就已经持有，
    #         # 或者在第 i-1 天卖出了股票并在第 i 天重新买入。状态转移方程为：
    #         hold[i] = max(hold[i - 1], cash[i - 1] - prices[i])
    #         # 如果我们在第 i 天不持有股票，可能是因为我们在第 i-1 天就不持有，
    #         # 或者在第 i-1 天持有股票并在第 i 天卖出。状态转移方程为：
    #         cash[i] = max(cash[i - 1], hold[i - 1] + prices[i] - fee)

    #     # 3. 提取结果
    #     return cash[n - 1]

    def maxProfit(self, prices: List[int], fee: int) -> int:
        """The transaction fee is only charged once for each stock purchase and sale.
        method2：股票买入时支付。
        """
        # 1. 初始化
        n = len(prices)
        hold = [0] * n  # 表示在第 i 天持有股票的最大利润。
        cash = [0] * n  # 表示在第 i 天不持有股票的最大利润。

        hold[0] = -prices[0] - fee  # 第一天买入股票并支付交易费用
        cash[0] = 0  # 第一天不持有股票

        # 2. 填充表格 - 确定状态转移方程
        for i in range(1, n):
            # 如果我们在第 i 天持有股票，可能是因为我们在第 i-1 天就已经持有，
            # 或者在第 i-1 天卖出了股票并在第 i 天重新买入。状态转移方程为：
            hold[i] = max(hold[i - 1], cash[i - 1] - prices[i] - fee)
            # 如果我们在第 i 天不持有股票，可能是因为我们在第 i-1 天就不持有，
            # 或者在第 i-1 天持有股票并在第 i 天卖出。状态转移方程为：
            cash[i] = max(cash[i - 1], hold[i - 1] + prices[i])

        # 3. 提取结果
        return cash[n - 1]


# @lc code=end
