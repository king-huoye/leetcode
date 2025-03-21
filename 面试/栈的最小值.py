class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack=list()
        

    def push(self, x: int) -> None:
        self.stack.append(x)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        else:
            return None

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return min(self.stack)


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
