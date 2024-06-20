def quick_sort(arr, left, right):
    if left < right:
        pivot = partition(arr, left, right)
        quick_sort(arr, left, pivot - 1)
        quick_sort(arr, pivot + 1, right)
    return arr


def partition(arr, left, right):
    pivot = arr[left]
    while left < right:
        while left < right and arr[right] > pivot:
            right -= 1
        arr[left] = arr[right]  # exchange the value of element at left and right

        while left < right and arr[left] < pivot:
            left += 1  # util the element at left is less than pivot, move left pointer to right

        arr[right] = arr[left]

    arr[right] = pivot  # lastly, left == right, so assign pivot to arr[right]
    return right  # return the index of pivot


if __name__ == "__main__":
    disorder_arr = [6, 3, 9, 1, 7, 2, 5]
    order_arr = quick_sort(disorder_arr, 0, len(disorder_arr) - 1)
    print(order_arr)
