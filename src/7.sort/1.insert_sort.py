def insertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while key < arr[j] and j >= 0:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def binaryInsertSort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        low = 0
        high = i - 1
        # compare
        while low <= high:
            mid = (low + high) // 2
            if key > arr[mid]:
                low = mid + 1
            else:
                high = mid - 1
        # remove
        for j in range(i, low, -1):
            arr[j] = arr[j - 1]
        arr[low] = key
    return arr


def shellSort(arr):
    # It is complex and has poor performance, so it has no real value
    length = len(arr)
    temp = length // 2  # initial step size
    while temp > 0:
        for i in range(temp, length):
            j = i
            while j >= temp and arr[j - temp] > arr[j]:
                arr[j - temp], arr[j] = arr[j], arr[j - temp]
                j -= temp
        temp = temp // 2
    return arr


disorder_arr = [6, 3, 9, 1, 7, 2, 5]
# order_arr = insertSort(disorder_arr)
# print(order_arr) # [1, 2, 3, 5, 6, 7, 9]

# order_arr = binaryInsertSort(disorder_arr)
# print(order_arr)

order_arr = shellSort(disorder_arr)
print(order_arr)
