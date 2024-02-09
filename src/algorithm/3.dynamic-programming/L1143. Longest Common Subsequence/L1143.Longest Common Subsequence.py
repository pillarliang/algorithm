class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        # return self.solve_recursion(text1, text2, 0, 0)
        n = len(text1)
        m = len(text2)
        memo = [[-1] * m for _ in range(n)]
        return self.solve_memoization(text1, text2, 0, 0, memo)

    def solve_recursion(self, text1: str, text2: str, i: int, j: int):
        """Time Limit Exceeded in LeetCode"""
        if i == len(text1) or j == len(text2):
            return 0

        ans = 0

        if text1[i] == text2[j]:
            ans = 1 + self.solve(text1, text2, i + 1, j + 1)
        else:
            ans = max(
                self.solve(text1, text2, i, j + 1), self.solve(text1, text2, i + 1, j)
            )

        return ans

    def solve_memoization(self, text1, text2, i, j, memo):
        if i == len(text1) or j == len(text2):
            return 0

        if memo[i][j] != -1:
            return memo[i][j]

        ans = 0

        if text1[i] == text2[j]:
            ans = 1 + self.solve_memoization(text1, text2, i + 1, j + 1, memo)
        else:
            ans = max(
                self.solve_memoization(text1, text2, i, j + 1, memo),
                self.solve_memoization(text1, text2, i + 1, j, memo),
            )

        memo[i][j] = ans
        return memo[i][j]


text1 = "abcde"
text2 = "ace"

# text1 = "abc"
# text2 = "def"

print(Solution().longestCommonSubsequence(text1, text2))
