class Solution:
    def rob(self, nums: List[int]) -> int:
        def fun(nums):
            if len(nums)==0:
                return 0
            if len(nums)==1:
                return nums[0]
            if len(nums)==2:
                return max(nums[0],nums[1])
            dp=[0]*(len(nums))
            dp[0]=nums[0]
            dp[1]=max(nums[0],nums[1])
            for i in range(2,len(nums)):
                dp[i]=max(dp[i-1],dp[i-2]+nums[i])
            return dp[len(nums)-1]
        if len(nums)==1:
            return nums[0]
            #主要是截取两端数组
        array=nums[:len(nums)-1]
        array2=nums[1:]
        a=fun(array)
        b=fun(array2)
        return max(a,b)
        
