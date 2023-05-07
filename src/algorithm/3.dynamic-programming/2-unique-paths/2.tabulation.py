def uniquePaths(m: int, n: int) -> int:
    table = [[0] * (n + 1) for i in range(m + 1)]
    table[1][1] = 1

    for row_index, row in enumerate(table):
        for item_index, item in enumerate(row):
            if row_index + 1 <= m:
                table[row_index + 1][item_index] += item
            if item_index + 1 <= n:
                table[row_index][item_index + 1] += item

    return table[m][n]


print(uniquePaths(1, 1))  # 1
print(uniquePaths(2, 3))  # 3
print(uniquePaths(3, 2))  # 3
print(uniquePaths(2, 3))  # 3
print(uniquePaths(3, 3))  # 6
print(uniquePaths(18, 18))  # 2333606220
