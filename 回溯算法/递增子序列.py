class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        self.path=[]
        self.result=[]
        def backtracking(nums,startIndex):
            if len(self.path)>=2:
                self.result.append(self.path[:])
            se=set()
            for i in range(startIndex,len(nums)):
                if (self.path and nums[i]<self.path[-1]) or (nums[i] in se):
                    continue
                se.add(nums[i])#取过的记录一下
                self.path.append(nums[i])
                backtracking(nums,i+1)
                self.path.pop()
        backtracking(nums,0)
        return self.result
