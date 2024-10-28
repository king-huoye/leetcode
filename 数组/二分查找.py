
from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<right:
            middle = (int)((left + right) / 2)
            if nums[middle]==target:
                return middle
            elif nums[middle]>target:
                right=middle-1
            elif nums[middle]<target:
                left=middle+1
        return -1
so=Solution()
arr=[-1,0,3,5,9,12]
target=9
tmp=so.search(arr,target)
print(tmp)

# 采用左闭右闭原则
