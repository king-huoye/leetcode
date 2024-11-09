class Solution:
    def letterCombinations(self, digits: str) -> List[str]:

        self.result=[]
        self.path=''
        self.Map=['','','abc','def','ghi','jkl','mno','pqrs','tuv','wxyz'] #建立映射
        if len(digits)==0:
            return []
        def backtracking(digits,index):
            if index==len(digits):
                self.result.append(self.path)
                return 
            Di=int(digits[index])
            letter=self.Map[Di] #获取对应的字符串
            for i in range(len(letter)):
                self.path+=letter[i]
                backtracking(digits,index+1)
                self.path=self.path[:-1] #去掉最后一个元素
        backtracking(digits,0)
        return self.result
