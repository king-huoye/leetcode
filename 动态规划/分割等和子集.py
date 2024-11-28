class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
        target=(int)(sum/2)
        if sum%2!=0: #总和为奇数时，不可能划分为两个相等的子集
            return False
        dp=[0]*(target+1)
        dp[0]=0
        for i in range(len(nums)):
            for j in range(target,nums[i]-1,-1):
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
                if dp[target]==target:
                    return True
        return False
