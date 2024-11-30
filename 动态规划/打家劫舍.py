class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[0]*(len(nums))
        if len(nums)==1:
            return nums[0]
        if len(nums)==2:
            return  max(nums[0],nums[1])
        dp[0]=nums[0]
        dp[1]=max(nums[0],nums[1])#考虑偷1号，不一定是偷1，因为要考虑最大值
        for i in range(2,len(nums)):
            dp[i]=max(dp[i-1],dp[i-2]+nums[i])
        return dp[len(nums)-1]
