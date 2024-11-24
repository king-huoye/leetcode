class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[0]*n for _ in range(m)]
        for i in range(m):
            dp[i][0]=1
        for j in range(n):
            dp[0][j]=1 #向右走和向下走只有一条路径
        for i in range(1,len(dp)):
            for j in range(1,len(dp[i])):
                dp[i][j]=dp[i-1][j]+dp[i][j-1]
        return dp[m-1][n-1] #右下角单元格
