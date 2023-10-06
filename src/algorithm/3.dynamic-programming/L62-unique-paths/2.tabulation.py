# def uniquePaths(m: int, n: int) -> int:
#     table = [[0] * (n + 1) for i in range(m + 1)]
#     table[1][1] = 1

#     for row_index, row in enumerate(table):
#         for item_index, item in enumerate(row):
#             if row_index + 1 <= m:
#                 table[row_index + 1][item_index] += item
#             if item_index + 1 <= n:
#                 table[row_index][item_index + 1] += item

#     return table[m][n]

# print(uniquePaths(1, 1))  # 1
# print(uniquePaths(2, 3))  # 3
# print(uniquePaths(3, 2))  # 3
# print(uniquePaths(2, 3))  # 3
# print(uniquePaths(3, 3))  # 6
# print(uniquePaths(18, 18))  # 2333606220


class Solution_tabulation:
    """tabulation"""
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0] * (n + 1) for _ in range(m + 1)]
        table[1][1] = 1

        for idx_row in range(m + 1):
            for idx_col in range(n + 1):
                if idx_row + 1 <= m:
                    table[idx_row + 1][idx_col] += table[idx_row][idx_col]
                if idx_col + 1 <= n:
                    table[idx_row][idx_col + 1] += table[idx_row][idx_col]
        return table[m][n]
