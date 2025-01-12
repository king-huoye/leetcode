class TripleInOne:

    def __init__(self, stackSize: int):
        # 创建一个数组，存储三个栈
        self.stack = [None] * (3 * stackSize)
        # 每个栈的栈顶指针
        self.stackSize = stackSize
        self.tops = [-1, -1, -1]  # 初始化每个栈的栈顶为-1，表示栈是空的

    def push(self, stackNum: int, value: int) -> None:
        if self.tops[stackNum] < self.stackSize - 1:  # 检查栈是否已满
            self.tops[stackNum] += 1
            self.stack[stackNum * self.stackSize + self.tops[stackNum]] = value

    def pop(self, stackNum: int) -> int:
        if self.tops[stackNum] == -1:  # 栈为空
            return -1
        else:
            value = self.stack[stackNum * self.stackSize + self.tops[stackNum]]
            self.tops[stackNum] -= 1
            return value

    def peek(self, stackNum: int) -> int:
        if self.tops[stackNum] == -1:  # 栈为空
            return -1
        else:
            return self.stack[stackNum * self.stackSize + self.tops[stackNum]]

    def isEmpty(self, stackNum: int) -> bool:
        return self.tops[stackNum] == -1
