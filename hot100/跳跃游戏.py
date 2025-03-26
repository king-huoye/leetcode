class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums)==1:
            return True
        cover=0
        n=len(nums)
        for i in range(n):
            if i<=cover:
                cover=max(cover,i+nums[i])
            if cover>=n-1:
                return True
        return False
