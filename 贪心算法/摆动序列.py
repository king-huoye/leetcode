class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        cur=0
        pre=0
        if len(nums)==1:
            return 1
        if len(nums)==2 and nums[0]!=nums[1]:
            return 2
        if len(nums)==2 and nums[0]==nums[1]:
            return 1
        result=1 #默认最右面有一个峰值
        for i in range(len(nums)-1):
            cur=nums[i+1]-nums[i] #需要计算cur
            if (cur>0 and pre<=0) or (cur<0 and pre>=0):#注意平坡的情况就是pre为0的时候
                result+=1
                pre=cur
        return result
        
