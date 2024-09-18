## Dynamic Programming

### L509-Fibonacci Number
**[Description**](https://leetcode.com/problems/fibonacci-number/description/)**

**[Code]**
   * **[Memorization:](./01-fibonacci/1.memorization.py)**
   * **[Tabulation:](./01-fibonacci/2.tabulation.py)**



### L62-unique-paths
**[Description**](https://leetcode.com/problems/unique-paths/description/)**
**[Code]**
   * **[Memorization:](./L62-unique-paths/1.memorization.py)**
   * **[Tabulation:](./L62-unique-paths/2.tabulation.py)**


### L70-Climbing Stairs
**[Description**](https://leetcode.com/problems/climbing-stairs/submissions/1083431569/)**
**[Code](./70.climbing-stairs.py)**


### L746 - Min Cost Climbing Stairs
**[Description**](https://leetcode.com/problems/min-cost-climbing-stairs/submissions/1085042368/)**
**[Code](./746.min-cost-climbing-stairs.py)**

### L1143 - Longest Common Subsequence
**[Description**](https://leetcode.com/problems/longest-common-subsequence/description/?envType=study-plan-v2&envId=leetcode-75)**
**[Code](./L1143.%20Longest%20Common%20Subsequence/L1143.Longest%20Common%20Subsequence.py)**
**[Note]**
This is a "DP - **Multidimensional**" problem. The storage structure of the problem is a two-dimensional array.
The storage structure of the problem is a two-dimensional array

### L746 - Longest Common Subsequence
**[Description**]()**
**[Code]()**


### 01-knapback
可以重复多次放入是完全背包，而只能放入一次是01背包，

**初始化**
定义问题 ：我们需要一个二维表格 `dp[i][j]`，其中 i 表示考虑到第 i 件物品，j 表示当前背包的容量。`dp[i][j]` 的值表示在前 i 件物品中选择，且不超过容量 j 的情况下可以获得的最大价值。

表格大小 ：创建一个大小为 `(n+1) x (w+1)` 的二维数组 dp，其中 n 是物品数量，w 是背包的最大容量。

初始化表格 ：将 `dp[0][j]` 初始化为 0 表示当没有物品可选时，无论背包容量如何，价值都是 0。同样，`dp[i][0]` 也初始化为 0，表示当背包容量为 0 时，价值也是 0。

**状态转移方程**

对于每件物品，我们有两种选择：

1. **不选择第 `i` 件物品** ：
   - `dp[i][j] = dp[i-1][j]`：即最大价值与前 `i-1` 件物品在同样容量下的最大价值相同。

2. **选择第 `i` 件物品** （前提是 `j >= weight[i]`）：
   - `dp[i][j] = dp[i-1][j-weight[i]] + value[i]`：即最大价值等于在容量为 `j-weight[i]` 的情况下前 `i-1` 件物品的最大价值加上当前物品的价值。

最终的状态转移方程为：

`dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight[i]] + value[i])`

如果 `j < weight[i]`，则只能选择不放入第 `i` 件物品，即：`dp[i][j] = dp[i-1][j]`


### 完全背包问题
完全背包问题。我们可以使用动态规划来解决这个问题。下面是详细的解决思路：

**初始化：**
- **表格定义：**
我们使用一个一维数组 dp，其中 `dp[j]` 表示容量为 j 的背包可以获得的最大价值。数组的大小为 W + 1，因为背包容量从 0 到 W。
- **初始化表格的默认值：**
初始化 `dp[0] = 0`，因为当背包容量为0时，最大价值自然也是0。
其他位置初始化为0，因为在开始时，其他容量的最大价值尚未计算。

**迭代填充表格：**
- **定义状态转移方程：**
对于每个物品 i 和每个可能的容量 j，我们考虑是否将物品 i 放入背包。
如果选择放入物品 i，那么 `dp[j]` 可以更新为 `dp[j - weight[i]] + value[i]`，其中 `j - weight[i]` 是放入物品 i 后剩余的容量。
状态转移方程为：`dp[j] = max(dp[j], dp[j - weight[i]] + value[i])`。

- **遍历表格：**
首先，遍历每一个物品 i。
对于每个物品 i，遍历容量 j 从 `weight[i]` 到 W。这里我们从小到大遍历容量是因为每个物品可以放入多次，以确保每个 `dp[j]` 都是基于当前物品的最新状态。

- **填充表格：**
对于每个物品和每个可能的容量，使用状态转移方程更新 `dp[j]`。

**提取结果：**
最终结果即为 `dp[W]`，表示背包容量为 W 时可以获得的最大价值。
