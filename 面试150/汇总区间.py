class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n=len(nums)
        i=0
        result=[]
        while i<n:
            low=i 
            i+=1
            while i<n and nums[i]==nums[i-1]+1:
                i+=1
            high=i-1 
            if low==high:
                result.append(str(nums[low]))
            else:
                result.append(f'{nums[low]}->{nums[high]}')
        return result
