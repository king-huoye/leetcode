class SortedStack:

    def __init__(self):
        self.stack=[]
        heapq.heapify(self.stack) #转为堆结构

    def push(self, val: int) -> None:
        heapq.heappush(self.stack,val)

    def pop(self) -> None:
        if self.stack:
            heapq.heappop(self.stack)

    def peek(self) -> int:#只是获取不是弹出，弹出后加入
        a=-1
        if self.stack:
            a=heapq.heappop(self.stack)#先弹出
            heapq.heappush(self.stack,a)#在推到堆中
        return a

    def isEmpty(self) -> bool:
        return not self.stack


# Your SortedStack object will be instantiated and called as such:
# obj = SortedStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.peek()
# param_4 = obj.isEmpty()
