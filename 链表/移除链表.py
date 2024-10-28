from typing import Optional

from Cython.Compiler.ExprNodes import ListNode

# 链表题在leetcode跑通,然后在notion做好笔记就好了
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head #指向头节点
        cur=dummy   #暂存的
        while cur.next!=None:
            if cur.next.val==val:
                cur.next=cur.next.next
            else:
                cur=cur.next
        return dummy.next #因为dummy下一个是头节点

so=Solution()
print(so.removeElements([1,2,6,3,4,5,6],6))
