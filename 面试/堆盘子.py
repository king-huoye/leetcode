class StackOfPlates:

    def __init__(self, cap: int):
        self.stack=[]
        self.cap=cap

    def push(self, val: int) -> None:
        if self.cap==0:
            return 
        if not self.stack or len(self.stack[-1])==self.cap:
            self.stack.append([val])
        else:
            self.stack[-1].append(val)

    def pop(self) -> int:
        return self.popAt(len(self.stack)-1)

    def popAt(self, index: int) -> int:
        if not self.stack or index>=len(self.stack) or not self.stack[index]:
            return -1
        res=self.stack[index].pop()
        if not self.stack[index]:
            self.stack=self.stack[0:index]+self.stack[index+1:]
        return res
        


# Your StackOfPlates object will be instantiated and called as such:
# obj = StackOfPlates(cap)
# obj.push(val)
# param_2 = obj.pop()
# param_3 = obj.popAt(index)
