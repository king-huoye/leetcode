class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        def kadane_max(arr):
            curr=max_num=arr[0]
            for num in arr[1:]:
                curr=max(num,curr+num)
                max_num=max(max_num,curr)
            return max_num
        
        def kadane_min(arr):
            curr=min_num=arr[0]
            for num in arr[1:]:
                curr=min(num,curr+num)
                min_num=min(min_num,curr)
            return min_num

        total=sum(nums)
        max_normal=kadane_max(nums)
        min_normal=kadane_min(nums)
        if max_normal<0:
            return max_normal #全负数情况
        return max(max_normal,total-min_normal)
