def can_sum(target: int, numbers: list) -> int:
    table = [False] * (target + 1)
    table[0] = True
    for index, item in enumerate(table):
        if item is False:
            continue
        for num in numbers:
            if index + num <= target:
                table[index + num] = True

    return table[target]


print(can_sum(7, [2, 3]))  # True
print(can_sum(7, [5, 3, 4, 7]))  # True
print(can_sum(7, [2, 4]))  # False
print(can_sum(8, [2, 3, 5]))  # True
print(can_sum(300, [7, 14]))  # False
