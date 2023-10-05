"""recursion"""

# def uniquePaths(m: int, n: int) -> int:
#     if m < 1 or n < 1:
#         return 0
#     if m == 1 and n == 1:
#         return 1
#     return uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
"""memoization"""


def uniquePaths(m: int, n: int, memo={}) -> int:
    if (m, n) in memo:
        return memo[(m, n)]

    if m < 1 or n < 1:
        memo[(m, n)] = 0
        return memo[(m, n)]
    if m == 1 and n == 1:
        memo[(m, n)] = 1
        return memo[(m, n)]

    memo[(m, n)] = uniquePaths(m - 1, n) + uniquePaths(m, n - 1)
    return memo[(m, n)]


class Solution_recursion:
    """recursion: this method will exceed time limit in leetcode"""
    def uniquePaths(self, m: int, n: int) -> int:
        if n < 1 or m < 1:
            return 0
        if n == 1 and m == 1:
            return 1

        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)


class Solution_memoization:
    """memoization"""
    def uniquePaths(self, m: int, n: int, memo={}) -> int:
        if (m, n) in memo:
            return memo[(m, n)]
        if n < 1 or m < 1:
            # memo[(m, n)] = 0
            # return memo[(m, n)]
            return 0
        if n == 1 and m == 1:
            # memo[(m, n)] = 1
            # return memo[(m, n)]
            return 1

        memo[(m, n)] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(
            m, n - 1, memo)
        return memo[(m, n)]


print(uniquePaths(1, 1))  # 1
print(uniquePaths(2, 3))  # 3
print(uniquePaths(3, 2))  # 3
print(uniquePaths(2, 3))  # 3
print(uniquePaths(3, 3))  # 6
print(uniquePaths(18, 18))  # 2333606220
