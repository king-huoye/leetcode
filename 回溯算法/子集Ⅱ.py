class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        self.result=[]
        self.path=[]
        def backtracking(nums,startIndex):
            nums.sort()
            self.result.append(self.path[:])
            for i in range(startIndex,len(nums)):
                if i>startIndex and nums[i]==nums[i-1]:
                    continue
                self.path.append(nums[i])
                backtracking(nums,i+1)
                self.path.pop()
        backtracking(nums,0)
        return self.result
