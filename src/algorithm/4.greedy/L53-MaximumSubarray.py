from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        count = 0

        for item in nums:
            if count < 0:
                count = 0

            count += item
            max_sum = max(max_sum, count)

        return max_sum


# nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# nums = [1]
# nums = [5, 4, -1, 7, 8]
nums = [-1]
print(Solution().maxSubArray(nums))
