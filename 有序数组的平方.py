from typing import List

# class Solution:
#     def sortedSquares(self, nums: List[int]) -> List[int]:
#         for i in range(len(nums)):
#             nums[i]=nums[i]*nums[i]
#
#         return sorted(nums)
# so=Solution()
# print(so.sortedSquares([-4,-1,0,3,10]))

# 暴力法

# 双指针法

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n=len(nums)
        result=[0]*n #定义新数组,长度要一样
        k=n-1
        j=n-1
        i=0
        while i<=j:
            if nums[i]*nums[i]>nums[j]*nums[j]:
                result[k]=nums[i]*nums[i]
                k-=1
                i+=1
            else:
                result[k]=nums[j]*nums[j]
                k-=1
                j-=1

        return result

so=Solution()
print(so.sortedSquares([-4,-1,0,3,10]))
