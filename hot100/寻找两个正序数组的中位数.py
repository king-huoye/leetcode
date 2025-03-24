class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        for num in nums2:
            nums1.append(num)
        nums1.sort()
        n=len(nums1)
        if n%2==1:
            return nums1[(int)(n/2)]
        else:
            left=(int)(n/2)-1
            right=(int)(n/2)
            return (nums1[left]+nums1[right])/2
