# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #直接模拟
        list1=[]
        list2=[]
        cur1=l1
        cur2=l2
        while cur1:
            list1.append(cur1.val)
            cur1=cur1.next
        while cur2:
            list2.append(cur2.val)
            cur2=cur2.next
        s1=''
        s2=''
        for i in range(len(list1)):
            s1+=str(list1[i])
        for j in range(len(list2)):
            s2+=str(list2[j])
        List1=list(s1)
        List2=list(s2)
        List1[:]=List1[::-1]
        List2[:]=List2[::-1]
        num1=''.join(List1)
        num2=''.join(List2)
        target=(int)(num1)+(int)(num2)
        tmp=str(target)[::-1]
        dummy=ListNode()
        cur=dummy
        for i in range(len(tmp)):
            now=ListNode((int)(tmp[i]))
            cur.next=now
            cur=now
        return dummy.next
