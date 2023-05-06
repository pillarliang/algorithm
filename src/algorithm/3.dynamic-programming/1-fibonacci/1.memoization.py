"""recursion"""

# def fib(n: int) -> int:
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fib(n - 1) + fib(n - 2)
"""memoization"""


def fib(n: int, memo={}) -> int:
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1:
        return 1
    # make sure that every top level call and it's recursive tree shares the same memo object.
    memo[n] = fib(n - 1, memo) + fib(n - 2, memo)
    return memo[n]
