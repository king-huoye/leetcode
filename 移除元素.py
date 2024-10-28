from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:

        slow=0
        n=len(nums)
        for i in range(n):
            if nums[i]!=val:
                nums[slow]=nums[i]
                slow+=1
        return slow
so=Solution()
array=[3,2,2,3]
n=so.removeElement(array,3)
print(n)





# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         while val in nums:
#             nums.remove(val)
#         return len(nums)
# so=Solution()
# array=[3,2,2,3]
# n=so.removeElement(array,3)
# print(n)

# class Solution:
#     def removeElement(self, nums: List[int], val: int) -> int:
#         l1=len(nums)
#         tmp=[]
#         for i in range(l1):
#             if nums[i]!=val:
#                 tmp.append(nums[i])
#         print(tmp)
#         return len(tmp)
#
# so=Solution()
# array=[0,1,2,2,3,0,4,2]
# n=so.removeElement(array,2)
# print(n)