class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count_0=nums.count(0)
        count_1=nums.count(1)
        count_2=nums.count(2)
        nums[:count_0]=[0]*count_0
        nums[count_0:count_0+count_1]=[1]*count_1
        nums[count_0+count_1:]=[2]*(count_2)
