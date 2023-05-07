def fib(n: int) -> int:
    table = [0] * (n + 1)
    table[0] = 0
    table[1] = 1

    for index, item in enumerate(table):
        if index + 1 <= n:
            table[index + 1] += item
        if index + 2 <= n:
            table[index + 2] += item

    return table[n]


print(fib(6))  # 8
print(fib(7))  # 13
print(fib(8))  # 21
print(fib(50))  # 12586269025
