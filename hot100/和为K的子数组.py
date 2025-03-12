class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        haxi=defaultdict(int)#记录前缀和出现次数
        haxi[0]=1
        sum=0　#维护前缀和
        count=0
        for i in range(len(nums)):
            sum+=nums[i]
            #检查是否存在前缀和
            if sum-k in haxi:
                count+=haxi[sum-k]
            haxi[sum]+=1
        return count
