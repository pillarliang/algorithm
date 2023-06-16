from typing import List


class Solution:
    def wiggleMaxLength_v1(self, nums: List[int]) -> int:
        pre_diff = 0  # record current element
        cur_diff = 0  # record current element
        mid_var = 0  # middle variable
        max_sub_seq = 1

        if len(nums) <= 1:
            return len(nums)

        for index in range(1, len(nums)):
            pre_diff = nums[index] - nums[index - 1]
            if index + 1 >= len(nums):
                # special case: the end element
                #   - flat
                #   - increase or decrease
                if pre_diff != 0 or (mid_var != 0 and pre_diff == 0):
                    max_sub_seq += 1

                return max_sub_seq

            cur_diff = nums[index + 1] - nums[index]
            if (pre_diff * cur_diff < 0) or (pre_diff == 0 and cur_diff != 0
                                             and mid_var * cur_diff < 0):
                max_sub_seq += 1

            if cur_diff != 0:
                mid_var = cur_diff

        return max_sub_seq

    def wiggleMaxLength_v2(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)

        pre_diff = 0  # record previous vaild element
        cur_diff = 0  # record current element
        max_sub_seq = 1

        for index in range(len(nums) - 1):
            cur_diff = nums[index + 1] - nums[index]

            if (pre_diff * cur_diff <= 0 and cur_diff != 0):
                max_sub_seq += 1
                pre_diff = cur_diff

        return max_sub_seq


# nums = [1, 7, 4, 9, 2, 5]
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# nums = [0, 0, 0]

print(Solution().wiggleMaxLength_v1(nums))
print(Solution().wiggleMaxLength_v2(nums))
