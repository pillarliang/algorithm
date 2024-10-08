"""
有 N 件物品和一个最多能背重量为 W 的背包。第i件物品的重量是weight[i]，得到的价值是value[i] 。
每件物品都有无限个（也就是可以放入背包多次），求解将哪些物品装入背包里物品价值总和最大。
"""


def complete_knapsack(W, weight, value):
    # 获取物品数量
    N = len(weight)

    # 初始化dp数组
    dp = [0] * (W + 1)

    # 遍历每一个物品
    for i in range(N):
        # 遍历每一个容量，从小到大遍历
        for j in range(weight[i], W + 1):
            # 更新dp数组
            dp[j] = max(dp[j], dp[j - weight[i]] + value[i])

    # 返回容量为W的最大价值
    return dp[W]


# 示例使用
weight = [2, 3, 4, 5]
value = [3, 4, 5, 6]
W = 10
print(complete_knapsack(W, weight, value))  # 输出应为15，选择3个重量为3的物品
