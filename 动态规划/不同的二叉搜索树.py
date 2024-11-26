class Solution:
    def numTrees(self, n: int) -> int:
        if n==0:
            return 1
        if n==1:
            return 1
        if n==2:
            return 2
        if n==3:
            return 5
        dp=[0]*(n+1)
        dp[0]=1
       
        for i in range(1,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]
