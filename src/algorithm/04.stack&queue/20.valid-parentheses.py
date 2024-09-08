#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#
# same as '../../data-structure/2.stack/3.bracket_check.py'


# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for item in s:
            if item == '[':
                stack.append(']')
            elif item == '(':
                stack.append(')')
            elif item == '{':
                stack.append('}')
            elif not stack or stack[-1] != item:
                return False
            else:
                stack.pop()

        return True if not stack else False


# @lc code=end

# s = "()[]{}"
s = "(]"
print(Solution().isValid(s))
