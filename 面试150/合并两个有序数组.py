class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:]=nums1[:m]
        for i in range(len(nums2)):
            nums1.append(nums2[i])
        nums1.sort()
        
