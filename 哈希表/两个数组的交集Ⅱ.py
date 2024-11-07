class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1.sort()
        nums2.sort()
        i=0
        j=0
        result=[]
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]:
                result.append(nums1[i])
                i+=1
                j+=1
            elif nums1[i]<nums2[j]:#数值小的指针后移
                i+=1
            else:
                j+=1
        return result
        
