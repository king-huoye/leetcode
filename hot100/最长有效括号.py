class Solution:
    def longestValidParentheses(self, s: str) -> int:
        if not s:
            return 0
        if len(s)==0:
            return 0
        n=len(s)
        stack=[-1]#应该计算坐标
        max_len=0
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    max_len=max(max_len,i-stack[-1])
        return max_len
        
