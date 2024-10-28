class Solution:
    def removeDuplicates(self, s: str) -> str:
        result=[]
        for char in s:
            if result and char==result[-1]:#不为空,当前遍历等于栈顶,栈顶弹出
                result.pop()
            else:
                result.append(char)
        return ''.join(result)

        
