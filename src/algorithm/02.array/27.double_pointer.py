#
# @lc app=leetcode id=27 lang=python3
#
# [27] Remove Element
#
from typing import List


# @lc code=start
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        fast = 0 # 快指针用于遍历数组
        slow = 0 # slow 用来收集不等于 val 的值
        
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow +=1
        
        return slow
                
            
# @lc code=end

