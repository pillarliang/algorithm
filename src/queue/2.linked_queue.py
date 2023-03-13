class Node(object):
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next = next_node


class LinkedQueue(object):
    """不带头节点的链式队列"""

    def __init__(self) -> None:
        self.front = None
        self.rear = None

    def is_queue_empty(self):
        """判断队列是否为空"""
        if self.front is None:
            return True
        return False

    def enQueue(self, item):
        """入队"""
        new_node = Node(item)
        if self.front is None:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        return True

    def deQueue(self):
        """出队"""
        if self.is_queue_empty():
            return False
        cur = self.front
        self.front = cur.next
        if cur == self.rear:
            # 最后一个节点出队
            cur.front, cur.rear = None, None
        return True

    def get_head(self):
        """获取队头元素"""
        if self.is_queue_empty():
            return False
        return self.front.data

    def get_len(self):
        """获取队列元素长度"""
        len = 1
        cur = self.front
        while cur.next and cur != self.rear:
            len += 1
            cur = cur.next
        return len


class LinkedQueueWithHead(object):
    """带头节点的链式队列"""

    def __init__(self) -> None:
        self.front = Node('head')
        self.rear = self.front

    def is_queue_empty(self):
        """判断队列是否为空"""
        if self.front == self.rear:
            return True
        return False

    def enQueue(self, item):
        """入队"""
        new_node = Node(item)
        self.rear.next = new_node
        self.rear = new_node
        return True

    def deQueue(self):
        """出队: 边界条件，只剩最后一个元素"""
        if self.is_queue_empty():
            return False
        cur = self.front.next
        self.front.next = cur.next
        if cur == self.rear:
            # 最后一个节点出队
            self.rear = self.front
        return True

    def get_head(self):
        """获取队头元素"""
        if self.is_queue_empty():
            return False
        return self.front.next.data

    def get_len(self):
        """获取队列元素长度"""
        len = 0
        cur = self.front
        while cur.next and cur != self.rear:
            len += 1
            cur = cur.next
        return len


queue = LinkedQueue()
queue.enQueue(2)
queue.enQueue(4)
queue.enQueue(6)

queue.deQueue()
print(queue.get_head())
print(queue.get_len())
