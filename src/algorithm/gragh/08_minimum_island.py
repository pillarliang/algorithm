def minimum_island(grid):
    visited = set()
    count = float('inf')

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            res = explore(grid, row, col, visited)
            if res and res < count:
                count = res

    return count


def explore(grid, row, col, visited):
    if not 0 <= row < len(grid) or not 0 <= col < len(grid[0]):
        return 0
    if grid[row][col] == 'W' or (row, col) in visited :
        return 0

    visited.add((row, col))

    num1 = explore(grid, row, col-1, visited)
    num2 = explore(grid, row, col+1, visited)
    num3 = explore(grid, row-1, col, visited)
    num4 = explore(grid, row+1, col, visited)

    return num1 + num2 + num3 + num4 + 1


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(minimum_island(grid))  # -> 2
