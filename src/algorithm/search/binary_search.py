def binary_search(arr, low, high, x):
    if (
        low <= high
    ):  # 因为在这里有限制，所以后面传给binary_search 的参数不需要在考虑下标范围了。
        mid = (low + high) // 2
        if x == arr[mid]:
            return mid
        elif x > arr[mid]:
            binary_search(arr, mid + 1, high, x)
        else:
            binary_search(arr, low, mid - 1, x)
    else:
        return -1


if __name__ == "__main__":
    arr = [3, 2, 7, 9, 1, 6]
    arr_sorted = sorted(arr)
    res = binary_search(arr_sorted, 0, len(arr), 6)
    print(res)
