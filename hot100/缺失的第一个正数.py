class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=1
        nums.sort()
        n=len(nums)
        for i in range(n):
            if nums[i]>0:
                if nums[i]==res:
                    res+=1
                elif nums[i]>res:
                    break
        return res
