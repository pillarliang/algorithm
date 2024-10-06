def complete_knapsack(W, weight, value):
    # 初始化
    dp = [0] * (W + 1)

    # 遍历每个物品
    for i in range(len(weight)):
        # 遍历背包容量， 从 weight[i] 到 W +1
        for j in range(weight[i], W + 1):
            # 更新 dp
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    return dp[W]


def complete_knapsack_2d(W, weight, value):
    N = len(weight)
    # 初始化 dp 数组
    dp = [[0] * (W + 1) for _ in range(N + 1)]

    # 遍历每个物品
    for i in range(1, N + 1):
        # 遍历背包容量
        for j in range(W + 1):
            if j >= weight[i - 1]:
                # 状态转移：考虑选或不选当前物品
                dp[i][j] = max(dp[i - 1][j], dp[i][j - weight[i - 1]] + value[i - 1])
            else:
                # 容量不足，不能选当前物品
                dp[i][j] = dp[i - 1][j]

    # 最终结果
    return dp[N][W]


# 示例用法
W = 10  # 背包容量
weight = [2, 3, 4]  # 每件物品的重量
value = [4, 5, 6]  # 每件物品的价值

max_value = complete_knapsack(W, weight, value)
print(f"最大价值为: {max_value}")  # 20
