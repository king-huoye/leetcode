from collections import Counter
from typing import List
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cou=dict()
        for i in range(len(nums)):
            if nums[i] in cou:
                cou[nums[i]]+=1
            else:
                cou[nums[i]]=1
        # print(cou)已经建立好字典了
        dui=[]#小顶堆
        for key,val in cou.items():
            heapq.heappush(dui,(val,key))#加到堆中
            if len(dui)>k:
                heapq.heappop(dui) #弹出最小的元素
        result=[]
        for i in range(len(dui)):
            result.append(dui[i][1])
        return result

so=Solution()
print(so.topKFrequent( nums = [1,1,1,2,2,3], k = 2))
