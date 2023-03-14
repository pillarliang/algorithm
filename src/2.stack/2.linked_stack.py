class Node(object):
    def __init__(self, data, next_node=None) -> None:
        self.data = data
        self.next = next_node


class LinkedStack(object):
    """用带头结点单链表实现栈"""

    def __init__(self) -> None:
        self.top = Node('head')
        self.size = 0

    def push(self, value):
        """增"""
        new_node = Node(value)
        new_node.next = self.top.next
        self.top.next = new_node
        self.size += 1

    def pop(self):
        """删"""
        if self.is_empty():
            return None
        value = self.top.next.data
        self.top.next = self.top.next.next
        self.size -= 1
        return value

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        return self.top.next.data

    def is_empty(self):
        """判空"""
        return self.size == 0

    def getSize(self):
        """栈长"""
        return self.size

    def __repr__(self) -> str:
        cur = self.top.next
        items = []
        while cur:
            items.append(cur.data)
            cur = cur.next
        return ' '.join(f'{num}' for num in items)


stack = LinkedStack()
print(stack.is_empty())

for i in range(9):
    stack.push(i)
print(stack)

for _ in range(3):
    stack.pop()
print(stack)

print(stack.getSize())
