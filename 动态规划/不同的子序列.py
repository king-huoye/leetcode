class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        dp=[[0]*(len(t)+1) for _ in range(len(s)+1)]
        for i in range(len(s)):
            dp[i][0]=1 #变成空字符串的方案
        dp[0][0]=1
        for i in range(1,len(s)+1):
            for j in range(1,len(t)+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j]+dp[i-1][j-1]
                else:
                    dp[i][j]=dp[i-1][j]
        return dp[len(s)][len(t)]
