class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(int)((left+right)/2)
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                left=middle+1
            elif nums[middle]>target:
                right=middle-1
        return left #多去模拟检查几次
        
