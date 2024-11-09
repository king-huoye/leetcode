class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        if min(candidates)>target:
            return []
        self.path=[]
        self.result=[]
        def backtracking(nums,targetSum,Sum,startIndex):
            if Sum>targetSum:
                return 
            if Sum==targetSum:
                self.result.append(self.path[:])
                return 
            for i in range(startIndex,len(nums)):
                Sum+=nums[i]
                 
                self.path.append(nums[i])
                backtracking(nums,targetSum,Sum,i)
                Sum-=nums[i]
                self.path.pop()#记得有弹出，回溯不可缺失的一部分
        backtracking(candidates,target,0,0)
        return self.result
