class MyQueue:

    def __init__(self):
        self.s_in=[] #主要负责push
        self.s_out=[] #主要负责pop
        

    def push(self, x: int) -> None:
        self.s_in.append(x) #入队操作
        

    def pop(self) -> int: #相当于出队
        if self.empty():#判断列表是否为空,两个都为空
            return None
        if self.s_out:#第二个列表不为空的花
            return self.s_out.pop()
        else:
            for i in range(len(self.s_in)):#输出栈为空导入数据
                self.s_out.append(self.s_in.pop())
            return self.s_out.pop()

        

    def peek(self) -> int:
        result=self.pop()
        self.s_out.append(result)
        return result
    def empty(self) -> bool:
        return not (self.s_in or self.s_out) #只要in或者out有元素说明队列不为空
