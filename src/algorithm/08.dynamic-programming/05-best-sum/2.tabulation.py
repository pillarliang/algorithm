def best_sum(target: int, numbers: list) -> int:
    table = [None] * (target + 1)
    table[0] = []
    for index, item in enumerate(table):
        if item is None:
            continue

        for num in numbers:
            if index + num <= target:
                if table[index + num] is None or (len(table[index + num]) >
                                                  len(item) + 1):
                    table[index + num] = item[:]
                    table[index + num].append(num)

    return table[target]


print(best_sum(7, [2, 3]))  # [3, 2, 2]
print(best_sum(7, [5, 3, 4, 7]))  # [7]
print(best_sum(7, [2, 4]))  # None
print(best_sum(8, [2, 3, 5]))  # [3, 5]
print(best_sum(300, [7, 14]))  # None
