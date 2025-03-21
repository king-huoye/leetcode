class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)]
        for i in range(n):
            dp[i][i]=1
        for i in range(n-1,-1,-1):
            for j in range(i+1,n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2#加入进去
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        return dp[0][n-1]#寻找整个字符串的最大长度
