from collections import deque


class MyStackDouble(object):
    """用两个队列实现"""

    def __init__(self) -> None:
        self.queue_in = deque()
        self.queue_out = deque()

    def push(self, x):
        self.queue_in.append(x)

    def pop(self):
        if self.empty():
            return None
        for _ in range(len(self.queue_in) - 1):
            self.queue_out.append(self.queue_in.popleft)

        self.queue_in, self.queue_out = self.queue_out, self.queue_in
        return self.queue_out.popleft()

    def top(self):
        if self.empty():
            return None
        return self.queue_in[-1]

    def empty(self):
        return len(self.queue_in) == 0


class MyStack(object):
    """使用一个队列实现"""

    def __init__(self) -> None:
        self.que = deque()

    def push(self, x):
        self.que.append(x)

    def pop(self):
        if self.empty():
            return None
        for _ in range(len(self.que) - 1):
            self.que.append(self.que.popleft())
        return self.que.popleft()

    def top(self):
        if self.empty():
            return None
        return self.que[-1]

    def empty(self):
        return not self.que
