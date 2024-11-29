class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp=[float('inf')]*(amount+1)
        dp[0]=0
        for i in range(len(coins)):
            for j in range(coins[i],amount+1):
                dp[j]=min(dp[j],dp[j-coins[i]]+1)
        
        if dp[amount]==float('inf'):# 如果最终背包容量的最小硬币数量仍为正无穷大，表示无解
            return -1
        else:
            return dp[amount]
