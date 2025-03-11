class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        stack=[]#使用栈去操作
      
        ans=0
        for i in range(len(s)):
            while s[i] in stack:
                stack.pop(0)
            stack.append(s[i])
            ans=max(ans,len(stack))
        return ans
