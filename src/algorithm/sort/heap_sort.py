def max_heapify(arr, n, i):
    largest = i  # Initialize largest as root
    left = 2 * i + 1
    right = 2 * i + 2

    # if left child is larger than root
    if left < n and arr[i] < arr[left]:
        largest = left

    # if right child is larger than root
    if right < n and arr[largest] < arr[right]:
        largest = right

    # if largest is not root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # recursively heapify the affected sub-tree
        max_heapify(
            arr, n, largest
        )  # 某个节点 i 不是最大值，并且交换了该节点和其子节点中的最大值之后，可能会破坏子树的堆性质。为了恢复堆的性质，需要对受影响的子树进行调整。


def build_max_heap(arr):
    """build max heap"""
    n = len(arr)
    for i in range(
        n // 2 - 1, -1, -1
    ):  # The index of the leaf node is from n // 2 to n - 1. so the last non-leaf node is n // 2 - 1.
        max_heapify(
            arr, n, i
        )  # for each non-leaf node, call heapify to make sure the subtree with the node as root satisfies the max heap property.


def heap_sort(arr):
    build_max_heap(arr)
    # 将堆顶元素（最大值）与堆的最后一个元素交换，然后调整剩余的堆，使其继续满足最大堆的性质。
    for i in range(len(arr) - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i, 0)


if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("排序前的数组:")
    print(arr)
    heap_sort(arr)
    print("排序后的数组:")
    print(arr)
