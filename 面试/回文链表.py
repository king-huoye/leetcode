class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if not head:
            return True
        cur=head
        res=[]
        while cur:
            res.append(cur.val)
            cur=cur.next
        return res==res[::-1]
        #直接比较数组翻转是否相同
