"""使用 python 内建的方法模拟队列"""
# 1. list
queue = []
queue.append('a')
queue.append('b')
queue.append('c')
queue.pop(0)
print(queue)  # ['b', 'c']

# 2.
from collections import deque

queue = deque()
queue.append('a')
queue.append('b')
queue.append('c')
queue.popleft()
print(queue)  # deque(['b', 'c'])

# 3.
from queue import Queue

queue = Queue(3)
queue.put('a')
queue.put('b')
queue.put('c')

print(queue.qsize())  # 3
print(queue.full())  # True
print(queue.get())  # a
print(queue.empty())  # False
