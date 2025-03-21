class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        self.path=[]
        self.result=[]
        def backtracking(nums,used):
            if len(self.path)==len(nums):
                self.result.append(self.path[:])
            for i in range(len(nums)):
                if used[i]:
                    continue
                used[i]=True
                self.path.append(nums[i])
                backtracking(nums,used)
                self.path.pop()
                used[i]=False
        n=len(nums)
        used=[False]*n #标志数组,记录哪些数字用过了
        backtracking(nums,used)
        return self.result
        
