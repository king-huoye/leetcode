from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result=[]
        nums.sort()
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            for i in range(k+1,len(nums)):
                 #前两个相加,后面逻辑要和三数之和的类似
                if i>k+1 and nums[i]==nums[i-1]:#去重
                    continue
                left=i+1
                right=len(nums)-1
                while left<right:
                    total=nums[i]+nums[k]+nums[left]+nums[right]
                    if total<target:
                        left+=1
                    elif total>target:
                        right-=1
                    else:
                        result.append([nums[k],nums[i],nums[left],nums[right]])
                        while left<right and nums[right]==nums[right-1]:
                            right-=1
                        while left<right and nums[left]==nums[left+1]:
                            left-=1
                        left+=1
                        right-=1
        return result

so=Solution()
print(so.fourSum(nums = [1,0,-1,0,-2,2], target = 0))
