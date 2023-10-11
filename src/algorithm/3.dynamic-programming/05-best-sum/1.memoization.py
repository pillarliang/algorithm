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

# def best_sum(targetSum, numbers, memo={}):
#     if targetSum in memo:
#         return memo[targetSum]

#     if targetSum < 0:
#         return None
#     if targetSum == 0:
#         return []
#     shortestCombination = None

#     for num in numbers:
#         remainderCombination = best_sum(targetSum - num, numbers, memo)

#         if remainderCombination is not None:
#             remainderCombination.append(num)
#             if (shortestCombination is None) or (len(remainderCombination) <
#                                                  len(shortestCombination)):
#                 shortestCombination = remainderCombination

#     memo[targetSum] = shortestCombination
#     return shortestCombination

# print(best_sum(7, [5, 3, 4, 7]))  # [7]
# print(best_sum(8, [2, 3, 5]))  # [3, 5]
# print(best_sum(8, [1, 4, 5]))  # [4, 4]
# print(best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]


class Solution:
    def best_sum(self, target, numbers, memo=None):
        if memo is None:
            memo = {}
        # 确保每次调用best_sum时（如果没有提供memo参数）都会创建一个新的、空的字典，从而避免了这个问题。

        if target in memo:
            return memo[target]

        if target == 0:
            return []
        if target < 0:
            return None

        shortest = None
        for num in numbers:
            res = self.best_sum(target - num, numbers, memo)
            if res is not None:
                # 创建一个新的组合，以防止修改原始的组合
                combination = res + [num]
                if (shortest is None) or (len(shortest) > len(combination)):
                    shortest = combination

        memo[target] = shortest
        return memo[target]


print(Solution().best_sum(7, [5, 3, 4, 7]))  # [7]
print(Solution().best_sum(8, [2, 3, 5]))  # [3, 5]
print(Solution().best_sum(8, [1, 4, 5]))  # [4, 4]
print(Solution().best_sum(100, [1, 2, 5, 25]))  # [25, 25, 25, 25]
