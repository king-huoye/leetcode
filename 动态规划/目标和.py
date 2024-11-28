class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        s=sum(nums)
        if (s+target)%2!=0:
            return 0
        Le=(int)((s+target)/2)
        dp=[0]*(1001)
        dp[0]=1
        for i in range(len(nums)):
            for j in range(Le,nums[i]-1,-1):
                dp[j]+=dp[j-nums[i]]
        return dp[Le]
