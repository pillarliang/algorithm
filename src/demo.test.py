# result = []
# result.append(1)
# result.append([1])
# print(result)

# print([1] + [2])

# from collections import deque

# a = deque([])
# a.append([])
# while a:
#     print(a)

# a = [1, 2]
# b = [2, 1]
# c = [2, 1]
# b.reverse()
# reversed(c)

# print(b)
# print(c)
# print(a == b)

# from itertools import product

# def get_grid_at_row_col(row, col):
#     row = row // 3 * 3
#     col = col // 3 * 3
#     return [product(range(row, row + 3), range(col, col + 3))]

# print(get_grid_at_row_col(1, 4))

# a = 1
# b = 2
# c = 3

# c = b < c or a

# print(c)

# a = [1]
# b = a
# # a.append(2)
# # b.append(3)
# # b = [2]

# print(a)
# print(b)

# print(id(a))
# print(id(b))

# b = [2]
# print(id(a))
# print(id(b))
# a = [1]
# print(id(a))

# a = [2]
# print(id(a))


# a = "hello"
# b = 42
# c = {}
# d = [a, b, c]

# d[1] = 0
# print(d)

# item = [1]
# color = ['red', item, 'black']
# color[1] = 'green'
# print(color)  # ['red', 'green', 'black']

# a = (1, 2)
# b = (1, 2)
# print(a == b)

# c = [1, 2]
# d = [1, 2]
# print(c == d)

# class Solution:
#     def tribonacci(self, n: int) -> int:
#         if n == 0:
#             return 0
#         elif n <= 2:
#             return 1

#         table = [0] * (n+1)
#         table[0] = 0
#         table[1] = 1

#         for i in range(1, n+1):
#             if i+1 < n:
#                 table[i+1] += table[i]
#             if i+2 < n:
#                 table[i+2] += table[i]
#             if i+3 < n:
#                 table[i+3] += table[i]

#         return table[n]


# print(Solution().tribonacci(4))

# item = [0, 0]
# item[0] = 1
# print(item)

from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        res = []

        while points:
            item = points[0]
            delete = []
            for index in range(1, len(points)):
                if points[index][0] <= item[0] and points[index][1] >= item[1]:
                    delete.append(points[index])
                    continue
                elif points[index][0] >= item[0] and points[index][1] <= item[1]:
                    item[0] = points[index][0]
                    item[1] = points[index][1]
                    delete.append(points[index])
                    continue
                elif points[index][0] <= item[0] <= points[index][1]:
                    item[1] = points[index][1]
                    delete.append(points[index])
                elif points[index][0] <= item[1] <= points[index][1]:
                    item[0] = points[index][0]
                    delete.append(points[index])
            for item in delete:
                points.remove(item)
            points.pop(0)
            res.append(item)
        return len(res)


# points = [[1, 2], [2, 3], [3, 4], [4, 5]] # 2
# points = [[10, 16], [2, 8], [1, 6], [7, 12]] # 2
# points = [[1, 2], [3, 4], [5, 6], [7, 8]]  # 4
points = [[3, 9], [7, 12], [3, 8], [6, 8], [
    9, 10], [2, 9], [0, 9], [3, 9], [0, 6], [2, 8]]

# print(Solution().findMinArrowShots(points))


print(sorted(points))
