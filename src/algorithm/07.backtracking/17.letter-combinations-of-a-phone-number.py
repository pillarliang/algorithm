#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#
from typing import List
from string import ascii_lowercase as alc


# @lc code=start
class Solution:
    def __init__(self):
        self.letterMap = [
            "",  # 0
            "",  # 1
            "abc",  # 2
            "def",  # 3
            "ghi",  # 4
            "jkl",  # 5
            "mno",  # 6
            "pqrs",  # 7
            "tuv",  # 8
            "wxyz"  # 9
        ]
        self.result = []
        self.s = ""

    def letterCombinations(self, digits: str) -> List[str]:
        # 
    
    def backtracking(self, digits, index):
        if len(digits) == index:
            self.result.append(self.s)
            return
        


# @lc code=end
digits = '23'
print(Solution().letterCombinations(digits))
