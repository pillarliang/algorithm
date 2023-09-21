#
# @lc app=leetcode id=459 lang=python3
#
# [459] Repeated Substring Pattern
#


# @lc code=start
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """brute force solution"""
        n = len(s)
        if n <= 1:
            return False

        substr = ""
        for i in range(1, n // 2 + 1):  # O(n)
            substr = s[:i]
            if substr * (n // i) == s:  # O(n)
                return True

        return False


class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        """串复制两次，去掉开头部分，看剩下字串中有没有原模式串。太妙了，但谁能想到..."""
        return s in (s + s)[1:-1]


# @lc code=end
# s = "abcabcabcabc"
s = "aba"
print(Solution().repeatedSubstringPattern(s))
