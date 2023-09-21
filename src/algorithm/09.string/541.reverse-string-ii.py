#
# @lc app=leetcode id=541 lang=python3
#
# [541] Reverse String II
#


# @lc code=start
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count = 0
        while count < len(s):
            count2 = count + k
            s = s[:count] + s[count:count2][::-1] + s[count2:]
            count = count2 + k
        return s


# @lc code=end
# s = "abcdefg"
# k = 2

s = "abcd"
k = 2
print(Solution().reverseStr(s, k))
