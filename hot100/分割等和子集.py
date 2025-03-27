class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums:
            return False
        n=len(nums)
        if sum(nums)%2!=0:
            return False
        amount=int(sum(nums)/2)#看能否装满
        dp=[0]*(amount+1)
        #只能用一次
        for i in range(len(nums)):
            for j in range(amount,nums[i]-1,-1):
                #看能否装满
                dp[j]=max(dp[j],dp[j-nums[i]]+nums[i])
                if dp[j]==amount:
                    return True
        return False   
