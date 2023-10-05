"""recursion"""

# def best_sum(targetSum, numbers):
#     if targetSum < 0:
#         return None
#     if targetSum == 0:
#         return []
#     shortestCombination = None

#     for num in numbers:
#         remainderCombination = best_sum(targetSum - num, numbers)

#         if remainderCombination is not None:
#             remainderCombination.append(num)
#             if (shortestCombination is None) or (len(remainderCombination) <
#                                                  len(shortestCombination)):
#                 shortestCombination = remainderCombination

#     return shortestCombination
"""memoization"""


def best_sum(targetSum, numbers, memo={}):
    if targetSum in memo:
        return memo[targetSum]

    if targetSum < 0:
        return None
    if targetSum == 0:
        return []
    shortestCombination = None

    for num in numbers:
        remainderCombination = best_sum(targetSum - num, numbers, memo)

        if remainderCombination is not None:
            remainderCombination.append(num)
            if (shortestCombination is None) or (len(remainderCombination) <
                                                 len(shortestCombination)):
                shortestCombination = remainderCombination

    memo[targetSum] = shortestCombination
    return shortestCombination


print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(8, [2, 3, 5]))  # [3, 5]
print(best_sum(8, [1, 4, 5]))  # [4, 4]
print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
