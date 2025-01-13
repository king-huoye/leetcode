# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        res1=[]
        res2=[]
        cur1=l1
        cur2=l2
        while cur1:
            res1.append(cur1.val)
            cur1=cur1.next
        while cur2:
            res2.append(cur2.val)
            cur2=cur2.next
        res1[:]=res1[::-1]
        res2[:]=res2[::-1]
        str1=''
        str2=''
        for i in res1:
            str1+=str(i)
        for j in res2:
            str2+=str(j)
        a=int(str1)
        b=int(str2)
        tmp=a+b
        temp=str(tmp)[::-1]
        l=len(temp)
        dummy=ListNode()
        cur=dummy
        for i in range(l):
            root=ListNode(int(temp[i]))
            cur.next=root
            cur=root
        return dummy.next
