class MinStack:

    def __init__(self):
        self.path = []
        self.min_stack = []
    def push(self, val: int) -> None:
        
        self.path.append(val)
        if not self.min_stack or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        if self.min_stack[-1] == self.path[-1]:
            self.min_stack.pop()
        self.path.pop()

    def top(self) -> int:
        return self.path[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
