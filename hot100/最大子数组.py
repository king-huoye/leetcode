class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        dp=[float('-inf')]*n 
        dp[0]=nums[0]
        for i in range(1,n):
            dp[i]=max(dp[i-1]+nums[i],nums[i])
        return max(dp)


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result=float('-inf')
        s=0
        for num in nums:
            s+=num
            if s>result:
                result=s 
            if s<0:
                s=0
        return result
