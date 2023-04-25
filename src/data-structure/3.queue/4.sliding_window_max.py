from collections import deque


def max_sliding_window(nums, k):
    nums_queue = deque(nums)  # 将输入数组转为队列
    max_queue = deque()  # 记录最大值
    result = []  # result 记录前k的元素的最大值
    for i in range(k):  # 先将前 k 的元素放进队列
        while max_queue and max_queue[-1] < nums[i]:
            # #如果push的数值大于入口元素的数值，那么就将队列后端的数值弹出，直到push的数值小于等于队列入口元素的数值为止。
            # 这样就保持了队列里的数值是单调从大到小的了。
            max_queue.pop()
        max_queue.append(nums[i])

    result.append(max_queue[0])

    for i in range(k, len(nums_queue)):
        item = nums_queue.popleft()
        if item == max_queue[0]:
            max_queue.popleft()
        while max_queue and max_queue[-1] < nums[i]:
            max_queue.pop()
        max_queue.append(nums[i])

        result.append(max_queue[0])

    return result


nums = [1, -1]
k = 1
print(max_sliding_window(nums, k))
