class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result=[]
        nums=sorted(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                return result
            if i>0 and nums[i-1]==nums[i]:
                continue #跳过相同的元素以避免重复
            left=i+1
            right=len(nums)-1
            while left<right:
                total=nums[i]+nums[left]+nums[right]
                if total>0:
                    right-=1
                elif total<0:
                    left+=1
                else:
                    result.append([nums[i],nums[left],nums[right]])
                    #跳过相同的元素以避免重复
                    / 去重逻辑应该放在找到一个三元组之后，对b 和 c去重
                    while right>left and nums[right]==nums[right-1]:
                        right-=1
                    while right>left and nums[left]==nums[left+1]:
                        left+=1
                    // 找到答案时，双指针同时收缩
                    right-=1
                    left+=1
        return result
