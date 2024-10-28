from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i=0
        result=len(nums)
        if sum(nums)<target:
            return 0
        all=0
        for j in range(len(nums)):
            all+=nums[j]
            while all>=target:
                subL=j-i+1
                result=min(result,subL)
                all=all-nums[i]
                i+=1
        return result



So=Solution()
print(So.minSubArrayLen(7,[2,3,1,2,4,3]))
