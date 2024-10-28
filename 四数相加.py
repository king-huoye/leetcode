from typing import List

from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        result=defaultdict(int)
        tmp=0
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i]+nums2[j] in result:
                    result[nums1[i]+nums2[j]]+=1 #有的话在自增
                else:
                    result[nums1[i]+nums2[j]]=1 #如果没有先赋值为1
        count=0
        for i in range(len(nums3)):
            for j in range(len(nums4)):
                target=-(nums3[i]+nums4[j])
                if target in result:
                    count+=result[target]
        return count

so=Solution()
print(so.fourSumCount(nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]))


