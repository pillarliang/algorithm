## HashTable

#### 1. L242.Valid Anagram

**[Description](https://leetcode.com/problems/valid-anagram/description/)**

**[Code](./242.valid-anagram.py)**

#### 2. L349.Intersection of Two Arrays
**[Description](https://leetcode.com/problems/intersection-of-two-arrays/description/)**
**[Code](./349.intersection-of-two-arrays.py)**

#### 3. L349.Intersection of Two Arrays
**[Description](https://leetcode.com/problems/happy-number/description/)**
**[Code](./202.happy-number.py)**

#### 4. L1.Two Sum
**[Description](https://leetcode.com/problems/two-sum/description/)**
**[Code](./1.two-sum.py)**
**Note:**
If we establish a dictionary for the "nums" array first, the last element will overwrite the value of the first element, resulting in something like [3, 3]. Therefore, we should create a dictionary for the elements that have been visited but not yet used.
```
# issue
nums_dict = {}
for index, item in enumerate(nums):
    nums_dict[item] = index
```

```
# right way
nums_dict = dict()
for index, item in enumerate(nums):
    if target - item in nums_dict:
        return [nums_dict[target - item], index]
    nums_dict[item] = index
```

#### 5.4SUM II
**[Description](https://leetcode.com/problems/4sum-ii/description/)**
**[Code](./454.4-sum-ii.py)**
