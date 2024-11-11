class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.path=[]
        self.result=[]
        def backtracking(nums,startIndex):
            self.result.append(self.path[:])#第一步收集结果
            for i in range(startIndex,len(nums)):
                self.path.append(nums[i])#其他和之前的一样
                backtracking(nums,i+1)
                self.path.pop()
        backtracking(nums,0)
        return self.result
