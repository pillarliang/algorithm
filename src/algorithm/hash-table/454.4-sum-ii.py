#
# @lc app=leetcode id=454 lang=python3
#
# [454] 4Sum II
#

# @lc code=start
from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int],
                     nums3: List[int], nums4: List[int]) -> int:
        hashmap = dict()
        count = 0
        # use dictionary to store the sum of the first two numeric values
        for n1 in nums1:
            for n2 in nums2:
                hashmap[n1 + n2] = hashmap.get(n1 + n2, 0) + 1

        # check if the last two values match the opposite of the fist two value
        for n3 in nums3:
            for n4 in nums4:
                if -(n3 + n4) in hashmap:
                    count += hashmap.get(-(n3 + n4))

        return count


# @lc code=end
# nums1 = [1, 2]
# nums2 = [-2, -1]
# nums3 = [-1, 2]
# nums4 = [0, 2]

nums1 = [0]
nums2 = [0]
nums3 = [0]
nums4 = [0]
print(Solution().fourSumCount(nums1, nums2, nums3, nums4))
