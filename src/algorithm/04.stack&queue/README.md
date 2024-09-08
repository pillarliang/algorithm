## Stack

#### 1. L20.Valid Parentheses

**[Description**](https://leetcode.com/problems/valid-parentheses/description/)**

**[Code](./20.valid-parentheses.py)**

**Note:** 妙处在于不是用下面这种冗余的代码。而是将前部分另一半存入栈，后续对于后半部分只需要判断是否相等即可。
```
if item =='(':
    s.append(item)
elif item == ')':
    if item[-1] == '(':
        s.pop()
    else:
        return False
elif item == '}':
    ...
```

#### [1047] Remove All Adjacent Duplicates In String
**[Description**](https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/description/)**

**[Code](./1047.remove-all-adjacent-duplicates-in-string.py)**