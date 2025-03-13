class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[1]*n 
        left=1
        for i in range(n):
            #左边开始算
            res[i]=left
            left*=nums[i]
        right=1
        for i in range(n-1,-1,-1):
            res[i]*=right
            right*=nums[i]
        return res
