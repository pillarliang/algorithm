#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
from collections import Counter

# class Solution:
#     def isHappy(self, n: int) -> bool:
#         n_count = Counter()
#         num = n
#         while num not in n_count:
#             n_count[num] = 1
#             # num_arr = [int(i) for i in list(str(num))]
#             # num_sum = 0
#             # for i in num_arr:
#             #     num_sum += pow(i, 2)
#             num_sum = sum([int(i) for i in list(str(num))])

#             if num_sum == 1:
#                 return True
#             num = num_sum
#         return False

# n = 19
# print(Solution().isHappy(n))


# # optimize
class Solution2:
    def isHappy(self, n: int) -> bool:
        record = set()
        while n not in record:
            record.add(n)
            num_sum = sum([int(i) for i in list(str(n))])

            if num_sum == 1:
                return True
            n = num_sum
        return False


n = 19
print(Solution2().isHappy(n))
