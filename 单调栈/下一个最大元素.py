class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result=[-1]*len(nums1)
        stack=[]
        stack.append(0)
        ma=dict()
        for i in range(len(nums1)):
            ma[nums1[i]]=i 
        for i in range(1,len(nums2)):
            while stack and nums2[i]>nums2[stack[-1]]:
                if nums2[stack[-1]] in ma:
                    index=ma[nums2[stack[-1]]]
                    result[index]=nums2[i]
                stack.pop()
            stack.append(i)
        return result
        
