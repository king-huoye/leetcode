class Solution:
    def numSquares(self, n: int) -> int:
        if n<=0:
            return 0
        dp=[float('inf')]*(n+1)
        dp[0]=0
        x=int(n**0.5)
        for i in range(1,x+1):
            for j in range(i*i,n+1):
                dp[j]=min(dp[j],dp[j-i*i]+1)
        return dp[n]
