class Solution_recursion:
    """recursion"""
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n
        return self.fib(n - 1) + self.fib(n - 2)


class Solution_memorization:
    """memoization"""
    def fib(self, n, memo={}):
        if n in memo:
            return memo[n]

        if n == 0 or n == 1:
            return n
        # make sure that every top level call and it's recursive tree shares the same memo object.
        memo[n] = self.fib(n - 1, memo) + self.fib(n - 2, memo)
        return memo[n]
