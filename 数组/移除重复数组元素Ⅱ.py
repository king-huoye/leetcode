class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        if n==1:
            return 1
        if n==2:
            return 2
        slow=2
        fast=2
        while fast<n:
            if nums[slow-2]!=nums[fast]:
                nums[slow]=nums[fast]
                slow+=1
            fast+=1
        return slow

        
