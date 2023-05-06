class MinStack:
    def __init__(self):
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        # pushes val onto stack
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)

    def pop(self) -> None:
        # removes val from top of stack
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # returns top of stack
        return self.stack[-1]

    def getMin(self) -> int:
        # returns min num in stack
        return self.minStack[-1]