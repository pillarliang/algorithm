#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

import re


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        a = re.split(r"\s+", s.strip())
        a.reverse()
        return " ".join(a)


class Solution2:
    def reverseWords(self, s: str) -> str:
        s_list = s.split()
        l = 0
        r = len(s_list) - 1

        while l < r:
            s_list[l], s_list[r] = s_list[r], s_list[l]
            l += 1
            r -= 1

        return " ".join(s_list)


# @lc code=end

# test
# s = "the sky is blue"
s = "  hello world  "
# s = "a good   example"
print(Solution2().reverseWords(s))
