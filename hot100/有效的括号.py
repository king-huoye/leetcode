class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(')')
            elif s[i]=='[':
                stack.append(']')
            elif s[i]=='{':
                stack.append('}')
            elif len(stack)==0 or stack[-1]!=s[i]:
                return False
            else:
                stack.pop()
        if len(stack)==0:
            return True
        else:
            return False
