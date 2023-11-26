def island_count(grid):
    visited = set()
    count = 0

    for row in range(len(grid)):
        for col in range(len(grid[0])):
            if explore(grid, row, col, visited):  # todo
                count += 1

    return count


def explore(grid, row, col, visited):
    if not (0 <= row < len(grid)) or not(0 <= col < len(grid[0])):
        return False
    if grid[row][col] == 'W':
        return False
    if (row, col) in visited:
        return False

    visited.add((row, col))

    explore(grid, row + 1, col, visited)
    explore(grid, row - 1, col, visited)
    explore(grid, row, col - 1, visited)
    explore(grid, row, col+1, visited)

    return True


grid = [
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'L', 'W', 'W', 'W'],
  ['W', 'W', 'W', 'L', 'W'],
  ['W', 'W', 'L', 'L', 'W'],
  ['L', 'W', 'W', 'L', 'L'],
  ['L', 'L', 'W', 'W', 'W'],
]

print(island_count(grid))  # -> 3