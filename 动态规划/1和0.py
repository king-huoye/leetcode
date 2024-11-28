class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp=[[0]*(n+1) for _ in range(m+1)]
        
        for char in strs:
            x=char.count('0')
            y=char.count('1')
            for i in range(m,x-1,-1):
                for j in range(n,y-1,-1):
                    dp[i][j]=max(dp[i][j],dp[i-x][j-y]+1)
        return dp[m][n]
        
