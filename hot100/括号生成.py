class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        self.result=[]
        def backtracking(S,left,right):
            if len(S)==2*n:
                self.result.append(''.join(S))

            if left<n:
                S.append('(')
                backtracking(S,left+1,right)
                S.pop()
            if right<left:
                S.append(')')
                backtracking(S,left,right+1)
                S.pop()
        backtracking([],0,0)
        return self.result
