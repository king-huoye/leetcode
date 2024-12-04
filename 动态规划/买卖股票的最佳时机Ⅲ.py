class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        dp=[[0]*5 for _ in range(len(prices))]
        dp[0][0]=0 #不操作
        dp[0][1]=-prices[0] #买入 
        dp[0][2]=0
        dp[0][3]=-prices[0]
        dp[0][4]=0
        for i in range(1,len(prices)):
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]-prices[i])
            dp[i][2]=max(dp[i-1][2],dp[i-1][1]+prices[i])
            dp[i][3]=max(dp[i-1][3],dp[i-1][2]-prices[i])
            dp[i][4]=max(dp[i-1][4],dp[i-1][3]+prices[i])
        return dp[len(prices)-1][4]
            
