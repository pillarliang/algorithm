class ArrayQueue(object):
    """用数组实现循环队列"""

    def __init__(self, capacity: int) -> None:
        self.data = []
        self.capacity = capacity
        self.front = 0  # 队头指针，出队+1
        self.rear = 0  # 队尾指针，入队+1

    def is_queue_empty(self):
        """判断队列是否为空"""
        if self.front == self.rear:
            return True
        return False

    def is_queue_full(self):
        """判断队列是否满"""
        if (self.rear + 1) % self.capacity == self.front:
            return True
        return False

    def enQueue(self, item):
        """进队"""
        if self.is_queue_full():
            return False
        self.data.insert(self.rear, item)
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deQueue(self):
        """出队"""
        if self.is_queue_empty():
            return False
        item = self.data[self.front]
        self.front = (self.front + 1) % self.capacity
        return item

    def get_head(self):
        """获取队头元素"""
        if self.is_queue_empty():
            return False
        return self.data[self.front]

    def get_len(self):
        """获取队列元素长度"""
        return (self.rear - self.front + self.capacity) % self.capacity


queue = ArrayQueue(5)
queue.enQueue(2)
queue.enQueue(4)
queue.enQueue(6)

queue.deQueue()
print(queue.get_head())
print(queue.get_len())
