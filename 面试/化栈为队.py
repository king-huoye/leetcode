class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue=deque()
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.queue:
            return self.queue.popleft()#弹出
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.queue:
            return self.queue[0]#队头元素
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        if len(self.queue)==0:
            return True
        else:
            return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
