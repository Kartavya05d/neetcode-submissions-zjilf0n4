class MinStack:

    def __init__(self):
        self.stack = []
        self.min = None

    def push(self, val: int) -> None:
        if self.min == None or val < self.min: self.min = val
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        if not self.stack: self.min = None
        else: self.min = min(self.stack)
        
    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min

        
