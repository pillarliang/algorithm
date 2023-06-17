# algorithm

## Data Structure

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
