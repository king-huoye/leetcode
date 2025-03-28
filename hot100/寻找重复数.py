class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        count=Counter(nums)
        for key,val in count.items():
            if val>=2:
                return key
