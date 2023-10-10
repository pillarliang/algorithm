# def how_sum(target: int, numbers: list) -> int:
#     table = [None] * (target + 1)
#     table[0] = []
#     for index, item in enumerate(table):
#         if item is None:
#             continue

#         for num in numbers:
#             if index + num <= target:
#                 table[index + num] = item[:]
#                 table[index + num].append(num)

#     return table[target]

# print(how_sum(7, [2, 3]))  # [3, 2, 2]
# print(how_sum(7, [5, 3, 4, 7]))  # [4, 3]
# print(how_sum(7, [2, 4]))  # None
# print(how_sum(8, [2, 3, 5]))  # [2, 2, 2, 2]
# print(how_sum(300, [7, 14]))  # None


class Solution:
    def how_sum(self, target, numbers):
        table = [None] * (target + 1)
        table[0] = []

        for i in range(target + 1):
            if table[i] is None:
                continue
            for num in numbers:
                if i + num <= target:
                    table[i + num] = table[i][:]
                    table[i + num].append(num)

        return table[target]


print(Solution().how_sum(7, [2, 3]))
print(Solution().how_sum(7, [5, 3, 4, 7]))
print(Solution().how_sum(7, [2, 4]))
