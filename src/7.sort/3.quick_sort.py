def quick_sort(arr, left, right):
    if left > right:
        return
    pivot = arr[left]
    low = left
    high = right
    while left < right:
        while left < right and arr[right] > pivot:
            right -= 1
        arr[left] = arr[right]

        while left < right and arr[left] < pivot:
            left += 1
        arr[right] = arr[left]
    arr[right] = pivot
    quick_sort(arr, low, left - 1)
    quick_sort(arr, left + 1, high)
    return arr


disorder_arr = [6, 3, 9, 1, 7, 2, 5]
order_arr = quick_sort(disorder_arr, 0, len(disorder_arr) - 1)
print(order_arr)
