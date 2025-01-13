class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        self.path=[]
        self.result=[]
        def backtracking(nums,index):
            self.result.append(self.path[:])
            for i in range(index,len(nums)):
                self.path.append(nums[i])
                backtracking(nums,i+1)
                self.path.pop()
        backtracking(nums,0)
        return self.result
