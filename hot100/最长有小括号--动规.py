class Solution:
    def longestValidParentheses(self, s: str) -> int:
        n=len(s)
        if n==0:
            return 0

        dp=[0]*n
        max_len=0
        for i in range(1,n):
            if s[i]==')':
                if s[i-1]=='(':
                    if i>=2:
                        dp[i]=dp[i-2]+2
                    else:
                        dp[i]=2
                elif s[i-1]==')':
                    if i-dp[i-1]-1>=0 and s[i-dp[i-1]-1]=='(':
                        dp[i]=dp[i-1]+(dp[i-2-dp[i-1]] if i-2-dp[i-1]>=0 else 0)+2
                max_len=max(max_len,dp[i])
        return max_len
