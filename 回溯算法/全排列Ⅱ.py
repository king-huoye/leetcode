class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        self.path=[]
        self.result=[]
        def backtracking(nums,used):
            nums.sort()
            if len(self.path)==len(nums):
                self.result.append(self.path[:])
            for i in range(0,len(nums)):
                if used[i] or (i>0 and nums[i]==nums[i-1] and not used[i-1]):#树层去重
                    continue
                self.path.append(nums[i])
                used[i]=True
                backtracking(nums,used)
                used[i]=False
                self.path.pop()
        used=[False]*len(nums)
        backtracking(nums,used)
        return self.result
