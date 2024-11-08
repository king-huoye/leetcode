class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        self.path=[]
        self.result=[]
        if k>n:
            return []
        def backtracking(targetSum,k,sum,startIndex):#startIndex表示下一层for循环搜索的起始位置
            if len(self.path)==k:
                if targetSum==sum:
                    self.result.append(self.path[:])#找到对应的路径
                    return 
            for i in range(startIndex,10):
                sum+=i
                if sum>targetSum:
                    return 
                self.path.append(i)
                backtracking(targetSum,k,sum,i+1)
                sum-=i
                self.path.pop()
        backtracking(n,k,0,1)
        return self.result
