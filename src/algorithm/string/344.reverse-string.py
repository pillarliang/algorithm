#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

# @lc code=start
from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        front, back = 0, len(s) - 1
        while front < back:
            s[front], s[back] = s[back], s[front]
            front += 1
            back -= 1


class Solution2:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()


class Solution3:
    def reverseString(self, s: List[str]) -> None:
        s[:] = reversed(s)


# @lc code=end
s = ["h", "e", "l", "l", "o"]
print(Solution2().reverseString(s))
