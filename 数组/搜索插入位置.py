class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left=0
        right=len(nums)-1
        for i in range(len(nums)):
            middle=(int)((left+right)/2)
            if nums[middle]==target:
                return middle
            elif nums[middle]<target:
                left=middle+1
            elif nums[middle]>target:
                right=middle-1
        return right+1 #指向最后一个比target小的元素的位置
