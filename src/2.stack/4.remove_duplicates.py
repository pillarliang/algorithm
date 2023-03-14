def remove_duplicates(str) -> str:
    """Remove All Adjacent Duplicates In String"""
    res = []
    for item in str:
        if res and res[-1] == item:
            res.pop()
        else:
            res.append(item)
    return ''.join(res)


print(remove_duplicates())
