class Solution:
    def jump(self, nums: List[int]) -> int:
        n=len(nums)
        if n==1:
            return 0
        count=0
        cur=0
        max_cover=0
        for i in range(n):
            cur=max(cur,i+nums[i])
            if i==max_cover:
                max_cover=cur
                count+=1
            if max_cover>=n-1:
                return count
