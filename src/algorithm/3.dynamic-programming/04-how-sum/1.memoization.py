"""recursion"""

# def how_sum(target, numbers):
#     if target < 0:
#         return None
#     if target == 0:
#         return []

#     for num in numbers:
#         remainderResult = how_sum(target - num, numbers)

#         if remainderResult is not None:
#             remainderResult.append(num)
#             return remainderResult
#     return None
"""memoization"""


def how_sum(target, numbers, memo={}):
    if target in memo:
        return memo[target]

    if target < 0:
        return None
    if target == 0:
        return []

    for num in numbers:
        remainderResult = how_sum(target - num, numbers, memo)

        if remainderResult is not None:
            remainderResult.append(num)
            memo[target] = remainderResult
            return remainderResult

    memo[target] = None
    return None


print(how_sum(7, [2, 3]))  # [3, 2, 2]
print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
print(how_sum(7, [2, 4]))  # None
print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
print(how_sum(300, [7, 14]))  # None
