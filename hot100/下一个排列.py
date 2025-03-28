from typing import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        
        # Step 1: 从右往左找到第一个升序对 nums[i] < nums[i + 1]
        i = n - 2
        while i >= 0 and nums[i] >= nums[i + 1]:
            i -= 1
        
        # Step 2: 如果找到了这样的 i
        if i >= 0:
            # Step 3: 从右往左找到第一个大于 nums[i] 的元素 nums[j]
            j = n - 1
            while j >= 0 and nums[j] <= nums[i]:
                j -= 1
            # 交换 nums[i] 和 nums[j]
            nums[i], nums[j] = nums[j], nums[i]
        
        # Step 4: 反转 i 之后的部分
        self.reverse(nums, i + 1, n - 1)
    
    # 辅助函数：反转数组的一部分
    def reverse(self, nums: List[int], left: int, right: int) -> None:
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1
