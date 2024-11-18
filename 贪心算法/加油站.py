class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        totalsum=0
        currentsum=0
        start=0
        for i in range(len(gas)):
            totalsum+=gas[i]-cost[i]
        if totalsum<0:
            return -1
        for i in range(len(gas)):
            currentsum=currentsum+(gas[i]-cost[i])
            if currentsum<0:
                currentsum=0
                start=i+1 #从下一个位置开始寻找
        return start
        
