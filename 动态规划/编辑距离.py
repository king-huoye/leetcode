class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1=len(word1)
        n2=len(word2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        for i in range(n1+1):
            dp[i][0]=i 
        for j in range(n2+1):
            dp[0][j]=j #初始化很关键
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+1)#word2添加一个元素相当于word1删除一个元素,最后一个代表替换
        return dp[n1][n2]
