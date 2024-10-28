class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        re=dict()
        for a in nums1:
            for b in nums2:
                if a+b in re:
                    re[a+b]+=1
                else:
                    re[a+b]=1
        
        count=0
        for c in nums3:
            for d in nums4:
                target=-c-d
                if target in re:
                    count+=re[target]
        return count

# # class Solution:
#     def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
#         result=defaultdict(int)
#         tmp=0
#         for i in range(len(nums1)):
#             for j in range(len(nums2)):
#                 if nums1[i]+nums2[j] in result:
#                     result[nums1[i]+nums2[j]]+=1 #有的话在自增
#                 else:
#                     result[nums1[i]+nums2[j]]=1 #如果没有先赋值为1
#         count=0
#         for i in range(len(nums3)):
#             for j in range(len(nums4)):
#                 target=-(nums3[i]+nums4[j])
#                 if target in result:
#                     count+=result[target]
#         return count
