class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result=[]
        self.path=[]
        def backtracking(nums,targetSum,sum,startIndex):
            nums.sort()
            if sum>targetSum:
                return 
            if sum==targetSum:
                self.result.append(self.path[:])
            for i in range(startIndex,len(nums)):
                if i>startIndex and nums[i]==nums[i-1]:#去重操作
                    continue 
                sum+=nums[i]
                self.path.append(nums[i])
                backtracking(nums,targetSum,sum,i+1)
                sum-=nums[i]
                self.path.pop()
        backtracking(candidates,target,0,0)
        return self.result
