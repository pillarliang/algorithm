# algorithm

## 数据结构

## 算法

### 枚举

#### [L204-Count Primes](./src/algorithm/1.Enumeration/L204-Count%20Primes.py)

原理：要得到自然数n以内的全部素数，必须把不大于的所有素数的倍数剔除，剩下的就是素数。

链接：https://leetcode.com/problems/count-primes/description/

```python
def countPrimes(n: int) -> int:
    if n < 2:
        return 0
    primes = [True] * n
    primes[0], primes[1] = False, False
    for i in range(2, int(n**0.5) + 1):
        # 把不大于的所有素数的倍数剔除
        if primes[i]:
            for j in range(i * i, n, i):
                # 这里需要注意，标记应该从 i*i 开始，而不是 2*i 开始。因为对于每个数 i 来说，枚举是从小到大的，
                # 此时前面数字的倍数都已经进行了标记。对于 i 而言，2*i 也肯定会被在枚举数字 2 时进行标记，[2,i) 区间的数同理。
                primes[j] = False

    return sum(primes)
```

