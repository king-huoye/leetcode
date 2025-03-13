class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n 
        nums.reverse()#先全部反转《然后在切片
        nums[:k]=reversed(nums[:k])
        nums[k:]=reversed(nums[k:])
    #如果可以开新数组就直接for循环（i+k)%n进行处理
