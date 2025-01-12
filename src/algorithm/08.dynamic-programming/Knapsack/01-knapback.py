"""
给定 n 件物品和一个容量为 w 的背包。
每件物品的重量是 weight[i]，价值是 value[i]。每件物品只能选择一次，求解如何选择物品装入背包以使得物品的总价值最大。
"""


def knapsack(n, w, weight, value):
    # 初始化 dp 数组
    table = [[0] * (w + 1) for _ in range(n + 1)]
    # table[i][j] 表示使用前 i 个物品，并且背包的总重量不超过 j 时的最大价值。

    # 填充 dp 数组
    for i in range(1, n + 1):
        for j in range(1, w + 1):
            if j >= weight[i]:
                # table[i - 1][j]: 不放当前物品的最大价值。
                # table[i - 1][j - weight[i]] + value[i]: 放当前物品后的最大价值。
                table[i][j] = max(
                    table[i - 1][j], table[i - 1][j - weight[i]] + value[i]
                )
            else:
                table[i][j] = table[i - 1][j]

    # 提取结果
    return table[n][w]


def knapsack_v2(n, w, weight, value):
    # 初始化 dp 数组
    table = [0] * (w + 1)
    # table[j] 表示背包的总重量不超过 j 时的最大价值。

    # 填充 dp 数组
    for i in range(1, n + 1):
        for j in range(w, weight[i] - 1, -1):
            table[j] = max(table[j], table[j - weight[i]] + value[i])

    # 提取结果
    return table[w]


# 示例调用
n = 4
w = 5
weight = [0, 2, 1, 3, 2]  # 添加一个0值，使索引从1开始
value = [0, 3, 2, 4, 2]  # 添加一个0值，使索引从1开始
print(knapsack(n, w, weight, value))  # 输出应为7
