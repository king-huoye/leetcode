# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        cur=head
        nums=[]
        while cur:
            nums.append(cur.val)
            cur=cur.next
        res=[0]*len(nums)
        n=len(nums)
        k=k%n #防止超过长度
        for i in range(len(nums)):
            #进行旋转变换
            res[(i+k)%n]=nums[i] #这里的旋转变换很重要
        dummy=ListNode()
        cur=dummy
        for i in range(len(res)):
            p=ListNode(res[i])
            cur.next=p
            cur=p
        return dummy.next
