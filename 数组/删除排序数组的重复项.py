#快慢指针法
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        slow=0
        for fast in range(1,len(nums)):
            if nums[fast]!=nums[slow]:
                slow+=1 #一直对这个顺序搞乱了
                nums[slow]=nums[fast]
        return slow+1
