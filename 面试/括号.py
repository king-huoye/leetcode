class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result=[]
        def backtracking(S,left,right):
            if len(S)==2*n:
                result.append(''.join(S))
                return #收集结果
            if left<n:
                S.append('(')
                backtracking(S,left+1,right)
                S.pop()
            if right<left:
                S.append(')')
                backtracking(S,left,right+1)
                S.pop()
        backtracking([],0,0) #left和right分别表示左括号和右括号的数量
        return result
