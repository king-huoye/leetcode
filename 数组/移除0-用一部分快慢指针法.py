class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow=0
        fast=0
        for fast in range(len(nums)):
            if nums[fast]!=0:
                nums[slow]=nums[fast]
                slow+=1 #把非0元素进行前移
        for t in range(slow,len(nums)):
            nums[t]=0 #slow指标后全部赋值为0
        return nums
