#
# @lc app=leetcode id=1047 lang=python3
#
# [1047] Remove All Adjacent Duplicates In String
#


# @lc code=start
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for item in s:
            if stack and stack[-1] == item:
                stack.pop()
            else:
                stack.append(item)

        return ''.join(stack)


# @lc code=end
# s = "abbaca"
s = "azxxzy"
print(Solution().removeDuplicates(s))
