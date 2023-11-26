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

a = (1, 2)
b = (1, 2)
print(a == b)

c = [1, 2]
d = [1, 2]
print(c == d)