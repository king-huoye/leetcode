class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        
        l, r = 0, len(nums) - 1
        first, last = nums[0], nums[-1]  # 预存首尾元素
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            
            # 判断 mid 落在哪个有序区间
            if nums[mid] >= first:  # 左半部分有序
                if first <= target < nums[mid]:
                    r = mid - 1  # target 在左边
                else:
                    l = mid + 1  # target 在右边
            else:  # 右半部分有序
                if nums[mid] < target <= last:
                    l = mid + 1  # target 在右边
                else:
                    r = mid - 1  # target 在左边
        
        return -1
##
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target not in nums:
            return -1
        return nums.index(target)
