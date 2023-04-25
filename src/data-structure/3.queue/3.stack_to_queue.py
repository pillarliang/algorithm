class MyQueue(object):
    """Implement Queue using Stacks.
    Leetcode:232"""

    def __init__(self) -> None:
        self.stack_in = []
        self.stack_out = []

    def push(self, x):
        self.stack_in.append(x)

    def pop(self):
        if self.empty():
            return None
        if self.stack_out:
            return self.stack_out.pop()
        else:
            for _ in range(len(self.stack_in)):
                self.stack_out.append(self.stack_in.pop())
            return self.stack_out.pop()

    def peek(self):
        ans = self.pop()
        self.stack_out.append(ans)
        return ans

    def empty(self):
        return not (self.stack_in or self.stack_out)
