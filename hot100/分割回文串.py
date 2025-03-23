class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.path=[]
        self.result=[]
        def backtracking(string,startIndex):
            if startIndex==len(string):
                self.result.append(self.path[:])
                return 
            for i in range(startIndex,len(string)):
                sub=s[startIndex:i+1]
                if sub==sub[::-1]:
                    self.path.append(sub)
                    backtracking(string,i+1)
                    self.path.pop()
        backtracking(s,0)
        return self.result
