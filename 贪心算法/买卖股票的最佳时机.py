class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=0
        for i in range(1,len(prices)):
            result+=max(prices[i]-prices[i-1],0)
        return result
      #
      class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result=[]
        for i in range(1,len(prices)):
            result.append(prices[i]-prices[i-1])
        sum=0
        for i in range(len(result)):
            if result[i]>0:
                sum+=result[i]
        return sum
