class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        result=[]
        for i in range(len(tokens)):
            if tokens[i]=='+' or tokens[i]=='-' or tokens[i]=='*' or tokens[i]=='/':
                num1=result.pop()
                num2=result.pop()
                if tokens[i]=='+':
                    result.append(num1+num2)
                elif tokens[i]=='-':
                    result.append(num2-num1)
                elif tokens[i]=='*':
                    result.append(num1*num2)
                elif tokens[i]=='/':
                    result.append(int(num2/num1))# 整数
            else:
                result.append(int(tokens[i]))
        tmp=result.pop()
        return tmp
