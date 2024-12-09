class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l1=len(s)
        l2=len(t)
        dp=[[0]*(l2+1) for _ in range(l1+1)]
        result=0
        for i in range(1,l1+1):
            for j in range(1,l2+1):
                if s[i-1]==t[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if dp[i][j]>result:
                    result=dp[i][j]
        if result==l1:
            return True
        else:
            return False
