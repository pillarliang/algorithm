#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#
from typing import List


# @lc code=start
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        solutions = []
        state = []
        self.search(state, solutions, n)
        return solutions

    def is_vaild_state(self, state, n):
        return len(state) == n

    def get_candidates(self, state, n):
        """find the next position in the state to populate"""
        candidates = set(range(n))
        position = len(state)

        # prune down candidates that place the queen into attacks
        for row, col in enumerate(state):
            # discard the column index if it's occupied by a queen
            candidates.discard(col)

            # discard diagonals
            dist = position - row
            candidates.discard(col + dist)
            candidates.discard(col - dist)
        return candidates

    def search(self, state, solutions, n):
        if self.is_vaild_state(state, n):
            state_to_string = self.state_to_string(state, n)
            solutions.append(state_to_string)
            return

        for candidate in self.get_candidates(state, n):
            state.append(candidate)
            self.search(state, solutions, n)
            state.remove(candidate)

    def state_to_string(self, state, n):
        # ex. [1, 3, 0, 2]
        # output: [".Q..","...Q","Q...","..Q."]
        res = []
        for i in state:
            string = '.' * i + 'Q' + '.' * (n - 1 - i)
            res.append(string)
        return res


# @lc code=end
n = 4
print(Solution().solveNQueens(n))
