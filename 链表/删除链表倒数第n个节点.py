class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy=ListNode()
        dummy.next=head
        tmp1=dummy
        count=0
        while tmp1.next:
            count+=1 #统计长度
            tmp1=tmp1.next
        if n<0 or n>count:
            return 
        cur=dummy
        cal=count-n #相当于下标
        while cal:
            cal-=1
            cur=cur.next
        cur.next=cur.next.next
        return dummy.next
