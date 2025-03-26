class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        count=Counter(nums)
        count_elment=count.most_common(k)
        res=[]
        for key,val in count_elment:
            res.append(key)
        return res
