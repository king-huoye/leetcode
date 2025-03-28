class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count=Counter(nums)
        res=count.most_common(1)[0][0]
        return res
