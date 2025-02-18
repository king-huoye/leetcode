class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        if len(prices)==1:
            return 0
        n=len(prices)
        dp=[[0]*2 for _ in range(n)]
        dp[0][0]=-prices[0]
        dp[0][1]=0
        for i in range(1,n):
            dp[i][0]=max(dp[i-1][0],dp[i-1][1]-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        return max(dp[n-1][0],dp[n-1][1])
        
