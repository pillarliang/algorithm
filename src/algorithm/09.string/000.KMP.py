def sub_str(haystack, needle):
    """Find the Index of the First Occurrence in a String
    暴力解法"""
    needle_len = len(needle)
    for i in range(len(haystack) - needle_len + 1):
        if haystack[i:i + needle_len] == needle:
            return i
    return -1


def index_KMP(haystack, needle):
    """KMP算法：主串和模式都是从1开始"""

    next = get_next(needle)
    j = 0
    for i in range(len(haystack)):
        # i: 主串指针
        # j: 模式串指针
        while j >= 1 and haystack[i] != needle[j]:
            # 当不匹配时，模式串指针回溯
            j = next[j - 1]
        if haystack[i] == needle[j]:
            # 继续比较后续字符
            j += 1
        if j == len(needle):
            # 匹配成功
            return i - len(needle) + 1
    return -1


def get_next(needle):
    """获取子串的 next 数组"""
    next = []
    next.append(0)
    for i in range(1, len(needle)):
        k = next[i - 1]
        while needle[i] != needle[k] and k != 0:
            k = next[k - 1]
        if needle[i] == needle[k]:
            next.insert(i, k + 1)
        else:
            next.insert(i, 0)
    return next


def getNext(needle):
    next = [0] * len(needle)
    j = 0
    next[0] = j
    for i in range(1, len(needle)):
        while j >= 1 and needle[i] != needle[j]:
            j = next[j - 1]
        if needle[i] == needle[j]:
            j += 1
        next[i] = j
    return next


def getnext2(needle):
    next = ['' for i in range(len(needle))]
    j, k = 0, -1
    next[0] = k
    while (j < len(needle) - 1):
        if k == -1 or needle[k] == needle[j]:
            k += 1
            j += 1
            next[j] = k
        else:
            k = next[k]
    return next


def getnext3(needle):
    next = ['' for i in range(len(needle))]
    k = -1
    next[0] = k
    for i in range(1, len(needle)):
        while (k > -1 and needle[k + 1] != needle[i]):
            k = next[k]
        if needle[k + 1] == needle[i]:
            k += 1
        next[i] = k
    return next


# haystack = "leetcode"
# needle = "leeto"

haystack = "aabaafaaca"
needle = "aafaac"
# print(f'next:{get_next(needle)}')
# print(f'next1:{getNext(needle)}')
# print(f'next:{getnext2(needle)}')
# print(f'next:{getnext3(needle)}')
# print(index_KMP(haystack, needle))

print(index_KMP(haystack, needle))
