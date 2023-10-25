#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#


# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        table = [0] * (n + 1)
        table[0] = 1
        ways = [1, 2]

        for index, item in enumerate(table):
            if item == 0:
                continue
            for way in ways:
                if index + way <= n:
                    table[index + way] += item

        return table[n]


class Solution2:
    def climbStairs(self, n: int) -> int:
        ways = [1, 2]
        if n == 0:
            return 1
        if n < 0:
            return None
        total_methods = 0
        for way in ways:
            res = self.climbStairs(n - way)
            if res:
                total_methods += res

        return total_methods


class Solution3:
    def climbStairs(self, n: int, memo={}) -> int:
        if n in memo:
            return memo[n]
        ways = [1, 2]
        if n == 0:
            return 1
        if n < 0:
            return None
        total_methods = 0
        for way in ways:
            res = self.climbStairs(n - way, memo)
            if res is None:
                return None
            total_methods += res
        memo[n] = total_methods
        return memo[n]


# @lc code=end
print(Solution2().climbStairs(3))
print(Solution2().climbStairs(2))
