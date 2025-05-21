class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        if not nums:
            return -1
        n=len(nums)
        if n==1:
            return 0
        elif n==2:
            max_num=max(nums)
            return nums.index(max_num)
        num=max(nums)
        if nums.index(num)==0:
            return 0
        elif nums.index(num)==n-1:
            return n-1
        for i in range(1,n):
            if i+1<n:
                if nums[i-1]<nums[i] and nums[i]>nums[i+1]:
                    return i 
        
##二分
from typing import List

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[mid + 1]:
                # 峰值在左侧（包括 mid）
                right = mid
            else:
                # 峰值在右侧
                left = mid + 1
        return left
