class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort(key=lambda x:abs(x),reverse=True)
        
        for i in range(len(nums)):
            if nums[i]<0 and k>0:
                k-=1
                nums[i]*=-1
        if k%2==1:
            nums[-1]*=-1
        return sum(nums)
