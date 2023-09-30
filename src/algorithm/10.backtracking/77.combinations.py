#
# @lc app=leetcode id=77 lang=python3
#
# [77] Combinations
#
from typing import List


# @lc code=start
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        self.backtracking(n, k, 1, [], result)
        return result

    def backtracking(self, n, k, startIndex, path, result):
        if len(path) == k:
            result.append(path[:])
            return

        for i in range(startIndex, n + 1):
            path.append(i)
            self.backtracking(n, k, i + 1, path, result)
            path.pop()
            # path.pop() e.g.:[1,2,3,4] k=2, [1,2] then pop 2 try [1,3]


# @lc code=end
n = 4
k = 2
print(Solution().combine(n, k))
