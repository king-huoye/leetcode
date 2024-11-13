class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.result=[]
        self.path=[]
        def backtracking(nums,used):
            t=len(nums)
            if len(self.path)==t:
                self.result.append(self.path[:])
                return 
            for i in range(0,len(nums)):
                if used[i]:
                    continue
                used[i]=True
                self.path.append(nums[i])
                backtracking(nums,used)
                used[i]=False
                self.path.pop()
        used=[False]*len(nums)
        backtracking(nums,used)
        return self.result
        
