class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        arr=nums+nums #注意这个扩充,不能是[nums]*2那样
        result=[-1]*(len(arr))
        stack=[]
        if not nums:
            return []
        stack.append(0)
        for i in range(1,len(arr)):
            while stack and arr[i]>arr[stack[-1]]:
                result[stack[-1]]=arr[i]
                stack.pop()
            stack.append(i)
        tmp=result[:len(nums)]
        return tmp
      ##
      class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        if not nums:
            return []
        stack=[]
        result=[-1]*(len(nums))
        n=len(nums)
        stack.append(0)
        for i in range(1,2*n):
            while stack and nums[i%n]>nums[stack[-1]]:
                result[stack[-1]]=nums[i%n]
                stack.pop()
            stack.append(i%n)
        return result
        
