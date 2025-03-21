class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        self.result=[]
        self.path=''
        dictionary=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
        def backtracking(digits,startIndex):
            if len(digits)==startIndex:
                self.result.append(self.path[:])
                return #收集完就够了
            num=int(digits[startIndex])#获取到数字
            dic=dictionary[num]
            for i in range(len(dic)):
                self.path+=dic[i]
                backtracking(digits,startIndex+1)
                self.path=self.path[:-1]
        if len(digits)==0:
            return []
        backtracking(digits,0)
        return self.result
        
