class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        n=len(prices)
        #想一下贪心
        max_profit=0
        min_price=float('inf')
        #要记录最小价格
        for pr in prices:
            max_profit=max(pr-min_price,max_profit)
            min_price=min(min_price,pr)
        return max_profit
