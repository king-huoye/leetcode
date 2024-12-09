class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #换成求最长子序列
        n1=len(word1)
        n2=len(word2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        result=0
        for i in range(n2+1):
            dp[0][i]=i 
        for j in range(n1+1):
            dp[j][0]=j #j次删除变一样
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1] #不删除,回退
                else:
                    dp[i][j]=min(dp[i-1][j]+1,dp[i][j-1]+1,dp[i-1][j-1]+2)
#分别是删word1,word2,两个都删除
        return dp[-1][-1]
  #换成判断求子序列的长度
  class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #换成求最长子序列
        n1=len(word1)
        n2=len(word2)
        dp=[[0]*(n2+1) for _ in range(n1+1)]
        result=0
        for i in range(1,n1+1):
            for j in range(1,n2+1):
                if word1[i-1]==word2[j-1]:
                    dp[i][j]=dp[i-1][j-1]+1
                else:
                    dp[i][j]=max(dp[i-1][j],dp[i][j-1])
                if result<dp[i][j]:
                    result=dp[i][j]
        return n1+n2-2*result
