class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(')')
            elif  s[i]=='[':
                stack.append(']')
            elif  s[i]=='{':
                stack.append('}')
            elif len(stack)==0 or stack[-1]!=s[i]: #遍历的时候栈已经空了，没有匹配的字符
                return False
            else:#匹配的时候弹出
                stack.pop()
        if len(stack)==0:#所有遍历完栈不为空
            return True
        else:
            return False     
