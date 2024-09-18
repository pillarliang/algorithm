#
# @lc app=leetcode id=416 lang=python3
#
# [416] Partition Equal Subset Sum
#
from typing import List


# @lc code=start
# class Solution:
#     def canPartition(self, nums: List[int]) -> bool:
#         total_sum = sum(nums)
#         if total_sum % 2 != 0:
#             return False

#         target = total_sum // 2
#         dp = [False] * (target + 1)
#         dp[0] = True  # 和为0总是可以通过选择空集来实现

#         for num in nums:
#             for j in range(target, num - 1, -1):
#                 dp[j] = dp[j] or dp[j - num]

#         return dp[target]


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2:
            return False
        target = sum(nums) // 2
        table = [False] * (target + 1)  # table[i] 表示原始列表中有没有元素和为 i
        table[0] = True

        for num in nums:
            for i in range(target, num - 1, -1):
                table[i] = (
                    table[i] or table[i - num]
                )  # 在本问题中对于任意列表元素，只要有和能到 i 就可。
        return table[target]


# @lc code=end

"""
事例说明：nums = [2,4,10]

# 从后向前遍历的原因：
sum = 16, 所以看数组中有没有元素和能等于 sum 的一半。逐个遍历元素，看减去元素值剩下的子问题是 True 还是 False
table[8] -> 2, table[6] 
table[8] -> 4, table[4]
table[8] -> 10 ✖


# 如果从小到大
table[0] = True # init
table[1] = False
table[2] = 2, table[0] # True
table[3] = 2, table[1] # False
table[4] = 2, table[2] # True # 因为每个元素只能使用一次，table[2]中已经用了 2 了，这里就不能再用了。
"""
