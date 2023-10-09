"""recursion"""

# def can_sum(target, numbers):
#     if target < 0:
#         return False
#     if target == 0:
#         return True
#     for num in numbers:
#         if can_sum(target - num, numbers):
#             return True

#     return False
"""memoization"""

# def can_sum(target, numbers, memo={}):
#     if target in memo:
#         return memo[target]

#     if target < 0:
#         return False
#     if target == 0:
#         return True
#     for num in numbers:
#         if can_sum(target - num, numbers, memo):
#             memo[target] = True
#             return True

#     memo[target] = False
#     return False

# print(can_sum(7, [2, 3]))  # True
# print(can_sum(7, [5, 3, 4, 7]))  # True
# print(can_sum(7, [2, 4]))  # False
# print(can_sum(8, [2, 3, 5]))  # True
# print(can_sum(300, [7, 14]))  # False

# def can_sum(target, numbers, memo={}):
#     if target in memo:
#         return memo[target]

#     if target == 0:
#         return True
#     if target < 0:
#         return False

#     for num in numbers:
#         memo[target] = can_sum(target - num, numbers, memo)
#         if memo[target]:
#             return True

#     memo[target] = False
#     return False

# print(can_sum(7, [2, 3]))  # True
# print(can_sum(7, [5, 3, 4, 7]))  # True
# print(can_sum(7, [2, 4]))  # False
# print(can_sum(8, [2, 3, 5]))  # True
# print(can_sum(300, [7, 14]))  # False


class Solution:
    def can_sum(self, target, numbers, memo={}):
        if target in memo:
            return memo[target]

        if target == 0:
            return True
        if target < 0:
            return False

        for num in numbers:
            memo[target] = self.can_sum(target - num, numbers, memo)
            if memo[target]:
                return True

        memo[target] = False
        return False


print(Solution().can_sum(7, [2, 3]))
print(Solution().can_sum(7, [5, 3, 4, 7]))
print(Solution().can_sum(7, [2, 4]))
print(Solution().can_sum(8, [2, 3, 5]))
print(Solution().can_sum(300, [7, 14]))
