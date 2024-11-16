class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        result=float('-inf')
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            if sum>result:
                result=sum
            if sum<0:#连续和为0,重新计算
                sum=0
        return result
        
