class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        nums.sort()
        n=len(nums)
        return nums[n-k]
