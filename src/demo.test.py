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

a = 1
b = 2
c = 3

c = b < c or a

print(c)
