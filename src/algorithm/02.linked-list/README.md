## Array

#### 1. L142.Linked List Cycle II

**[Description**](https://leetcode.com/problems/linked-list-cycle-ii/description/)**

**[Code](./142.linked-list-cycle-ii.py)**

**[Reference](https://programmercarl.com/0142.%E7%8E%AF%E5%BD%A2%E9%93%BE%E8%A1%A8II.html)**



#### 2. [L42. Trapping Rain Water](https://leetcode.com/problems/trapping-rain-water/)

**[Code](./42.%20Trapping%20Rain%20Water.py)**

**[Reference](https://www.youtube.com/watch?v=ZI2z5pq0TqA)**

Note:

核心：每一个位置能接到的水💦为左右两侧的短板减去该位置的高度。

- 接水的能力由左右两侧较短的决定。而左右两侧单独的高度则由两侧的最高节点决定。

- 左右两侧的短板：用双指针来获取。使用双指针遍历列表时间复杂度为`O(n)`。即：左右两侧指针没移动一个位置就在该位置计算，无需按顺序从左到右迭代计算。

#### 3. [2095. Delete the Middle Node of a Linked List](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/?envType=study-plan-v2&envId=leetcode-75)

双指针之快慢指针。