class Solution_tabulation:
    """tabulation"""
    def fib(self, n):
        table = [0] * (n + 1)
        table[0] = 0
        table[1] = 1

        for idx, item in enumerate(table):
            if idx + 1 <= n:
                table[idx + 1] += item
            if idx + 2 <= n:
                table[idx + 2] += item

        return table[n]


print(Solution_tabulation().fib(2))
