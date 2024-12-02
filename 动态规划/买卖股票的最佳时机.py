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
            dp[i][0]=max(dp[i-1][0],-prices[i])
            dp[i][1]=max(dp[i-1][1],dp[i-1][0]+prices[i])
        return max(dp[n-1][0],dp[n-1][1])

##贪心
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:  # 如果价格数组为空，直接返回0
            return 0
        
        # 初始化最小价格为第一个价格，最大利润为0
        min_price = prices[0]
        max_profit = 0
        
        # 从第二天开始遍历价格
        for price in prices[1:]:
            # 计算当前价格卖出时的利润
            profit = price - min_price
            # 更新最大利润
            max_profit = max(max_profit, profit)
            # 更新最小价格
            min_price = min(min_price, price)
        
        return max_profit
