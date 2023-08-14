# algorithm

## Data Structure
### [Array](./src/algorithm/array/README.MD)
### [Linked-list](./src/algorithm/linked-list/README.md)

## Algorithm

### Enumeration

#### [L204-Count Primes](./src/algorithm/1.Enumeration/L204-Count%20Primes.py)

原理：要得到自然数n以内的全部素数，必须把不大于的所有素数的倍数剔除，剩下的就是素数。

**Description**: https://leetcode.com/problems/count-primes/description/



### Recursion

#### [L2-Add Two Numbers](./src/algorithm/2.Recursion/L2-AddTwoNumbers.py)
**Description**: https://leetcode.com/problems/add-two-numbers/



### Dynamic Programming

#### L509-Fibonacci Number
**Description**: https://leetcode.com/problems/fibonacci-number/description/

**Method:**

- [memoization](./src/algorithm/3.dynamic-programming/fibonacci/1.memoization.py)



### Greedy

#### [L455-Assgin Cookies](./src/algorithm/4.greedy/L455-AssignCookies.py)
**Description**: https://leetcode.com/problems/assign-cookies/description/

**Method**: https://leetcode.com/problems/assign-cookies/description/two-ways-to-solve-this-problem-using-python3/




#### L376-Wiggle SubSequence
**[Description](https://leetcode.com/problems/wiggle-subsequence/description/)**

**[Code](../algorithm/src/algorithm/4.greedy/L376-wiggleSubsequence.py)**

**[Tutorial](https://programmercarl.com/0376.%E6%91%86%E5%8A%A8%E5%BA%8F%E5%88%97.html#%E6%80%9D%E8%B7%AF-1-%E8%B4%AA%E5%BF%83%E8%A7%A3%E6%B3%95)**

**Notes:** 

-  Local optimality is similar to the extrema of a function.
- 💡 To deal with peaks at both ends of the sequence, it is much easier to process **the first point** than **the last**.




#### L53-Maximum Subarray

**[Description](https://leetcode.com/problems/maximum-subarray/)**

**[Code](../algorithm/src/algorithm/4.greedy/L53-MaximumSubarray.py)**

**[Tutorial](https://programmercarl.com/0053.%E6%9C%80%E5%A4%A7%E5%AD%90%E5%BA%8F%E5%92%8C.html)**

**Notes:**

- 局部最优：当前“连续和”为负数的时候立刻放弃，从下一个元素重新计算“连续和”，因为负数加上下一个元素 “连续和”只会越来越小。
- 全局最优：选取最大“连续和”




#### L122-Best Time to Buy and Sell Stock II


**[Description](https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/)**

**[Code](../algorithm/src/algorithm/4.greedy/L122.%20Best%20Time%20to%20Buy%20and%20Sell%20Stock%20II.py)**

**[Tutorial](https://www.programmercarl.com/0122.%E4%B9%B0%E5%8D%96%E8%82%A1%E7%A5%A8%E7%9A%84%E6%9C%80%E4%BD%B3%E6%97%B6%E6%9C%BAII.html#%E6%80%9D%E8%B7%AF)**

**Notes:**

- 局部最优：收集每天的正利润，

- 全局最优：求得最大利润。

摆动序列：看的是极值的个数，不求极值的差；

买卖股票：看的是极小值与极大值的差，且极小值需在极大值之前。



#### L55-Jump Game

**[Decription](https://leetcode.com/problems/jump-game/description/)**

**[Code](./src/algorithm/4.greedy/L55.jump-game.py)**

**[Tutorial](https://www.programmercarl.com/0055.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8F.html#%E6%80%9D%E8%B7%AF)**

**Notes:**

关键在于：不用拘泥于每次究竟跳几步，而是看覆盖范围，覆盖范围内一定是可以跳过来的，不用管是怎么跳的。

- 局部最优：每次移动取最大跳跃步数

- 全局最优：最后得到整体最大覆盖范围，看是否能到终点。





#### L45-Jump Game II

**[Description](https://leetcode.com/problems/jump-game-ii/description/)**

**[Code](./src/algorithm/4.greedy/45.jump-game-ii.py)**

**[Tutorial](https://programmercarl.com/0045.%E8%B7%B3%E8%B7%83%E6%B8%B8%E6%88%8FII.html)** 只看文字，不要看代码

**Notes:**

**这里需要统计两个覆盖范围，当前这一步的最大覆盖和下一步最大覆盖**。

如果移动下标达到了当前这一步的最大覆盖最远距离了，还没有到终点的话，那么就必须再走一步来增加覆盖范围，直到覆盖范围覆盖了终点。

- 局部最优：当前可移动距离尽可能多走，如果还没到终点，步数再加一。

- 整体最优：一步尽可能多走，从而达到最小步数。



#### L1005-Maximize Sum Of Array After K Negations

**[Description](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/)**

**[Code](./src/algorithm/4.greedy/1005.maximize-sum-of-array-after-k-negations.py)**

**Notes:**

涉及两处贪心：

1.

- 局部最优：让绝对值大的负数变为正数，当前数值达到最大，
- 整体最优：整个数组和达到最大。

2.

- 局部最优：只找数值最小的正整数进行反转，当前数值和可以达到最大（例如正整数数组{5, 3, 1}，反转1 得到-1 比 反转5得到的-5 大多了），
- 全局最优：整个 数组和达到最大。





#### L-

**[Description](https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/description/)**

**[Code](./src/algorithm/4.greedy/1005.maximize-sum-of-array-after-k-negations.py)**

**[Tutorial](https://programmercarl.com/1005.K%E6%AC%A1%E5%8F%96%E5%8F%8D%E5%90%8E%E6%9C%80%E5%A4%A7%E5%8C%96%E7%9A%84%E6%95%B0%E7%BB%84%E5%92%8C.html)** 只看文字，不要看代码

**Notes:**





