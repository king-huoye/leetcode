from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        result={}
        for i in range(len(nums)):
            tmp=target-nums[i]
            if tmp in result:
                return [result[tmp],i]
            result[nums[i]]=i


so=Solution()
print(so.twoSum([3,2,4],6))



