class ArrayStack(object):
    def __init__(self) -> None:
        """没有设置栈顶指针——没必要。
        没有初设栈大小"""
        self.items = []

    def push(self, item):
        """增"""
        self.items.append(item)

    def pop(self):
        """删"""
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        """返回栈顶元素"""
        if self.is_empty():
            return None
        return self.items[-1]

    def is_empty(self):
        """判空"""
        return len(self.items) == 0

    def size(self):
        """栈长"""
        return len(self.items)
