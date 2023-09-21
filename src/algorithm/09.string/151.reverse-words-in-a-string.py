#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#

import re


# @lc code=start
class Solution:
    def reverseWords(self, s: str) -> str:
        a = re.split(r'\s+', s.strip())
        a.reverse()
        return ' '.join(a)


# @lc code=end

# test
# s = "the sky is blue"
s = "  hello world  "
# s = "a good   example"
print(Solution().reverseWords(s))
