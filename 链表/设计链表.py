class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:

    def __init__(self):
        self.dummy = ListNode()  # 虚拟头节点
        self.size = 0

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        cur = self.dummy.next  # 从第一个节点开始获取
        while index:
            cur = cur.next
            index -= 1
        return cur.val

    def addAtHead(self, val: int) -> None:
        p = ListNode(val)
        p.next = self.dummy.next
        self.dummy.next = p
        self.size += 1

    def addAtTail(self, val: int) -> None:
        cur = self.dummy
        while cur.next:
            cur = cur.next
        p = ListNode(val)
        cur.next = p
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:  # 修正条件，允许等于size
            return
        p = ListNode(val)
        cur = self.dummy
        while index:
            cur = cur.next
            index -= 1
        p.next = cur.next  # 插入节点
        cur.next = p
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        cur = self.dummy
        while index:
            cur = cur.next
            index -= 1
        cur.next = cur.next.next
        self.size -= 1
