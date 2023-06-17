from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res_sum = 0
        for index in range(len(prices) - 1):
            current = prices[index + 1] - prices[index]
            if current > 0:
                res_sum += current

        return res_sum


prices = [7, 1, 5, 3, 6, 4]
prices = [1, 2, 3, 4, 5]
prices = [7, 6, 4, 3, 1]
print(Solution().maxProfit(prices))
