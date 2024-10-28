from collections import deque
class MyStack:

    def __init__(self):
        self.que=deque()
        

    def push(self, x: int) -> None:
        self.que.append(x)
        

    def pop(self) -> int:
        if self.empty():
            return None
        for i in range(len(self.que)-1):
            self.que.append(self.que.popleft())#队首移除元素
        return self.que.popleft() #从队首移除元素
        

    def top(self) -> int:
        return self.que[-1]
        

    def empty(self) -> bool:
        return len(self.que)==0
