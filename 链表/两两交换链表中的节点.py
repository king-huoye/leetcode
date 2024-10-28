# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode() #创建虚拟节点
        dummy.next=head
        cur=dummy #获取当前虚拟节点
        #保存是保存后两个的元素
        while cur.next!=None and cur.next.next!=None: #一定是两种情况都要考虑
            tmp1=cur.next
            tmp2=cur.next.next.next
            cur.next=cur.next.next
            cur.next.next=tmp1
            tmp1.next=tmp2
            cur=cur.next.next
        return dummy.next
必须有cur的下一个和下下个才能交换，否则说明已经交换结束了
