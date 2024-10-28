class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast=head
        slow=head
        while fast!=None and fast.next!=None: #空节点以及是只有一个节点的情况
            fast=fast.next.next
            slow=slow.next
            if fast==slow:环内相遇后，此时从head 和 相遇点，同时查找直至相遇
                slow=head
                #重新考虑这里需要
                while slow!=fast:
                    slow=slow.next #只走一步
                    fast=fast.next
                return fast           
        return None
