#
# @lc app=leetcode id=28 lang=python3
#
# [28] Find the Index of the First Occurrence in a String
#


# @lc code=start
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        return haystack.find(needle)


# @lc code=end
# case1
# haystack = "sadbutsad"
# needle = "sad"

# case2
haystack = "leetcode"
needle = "leeto"
print(Solution().strStr(haystack, needle))
