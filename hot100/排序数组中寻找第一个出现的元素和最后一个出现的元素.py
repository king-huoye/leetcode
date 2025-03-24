class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1,-1]
        res=[]
        for i in range(len(nums)):
            if nums[i]==target:
                res.append(i)
        if not res:
            return [-1,-1]
        else:
            return [res[0],res[-1]]

  # 
  class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left=0
        right=len(nums)-1
        first=-1
        last=-1
        while left<=right:
            middle=(int)((left+right)/2)
            if nums[middle]==target:
                first=middle
                right=middle-1
            elif nums[middle]>target:
                right=middle-1
            else:
                left=middle+1
        left=0
        right=len(nums)-1
        while left<=right:
            middle=(int)((left+right)/2)
            if nums[middle]==target:
                last=middle
                left=middle+1
            elif nums[middle]>target:
                right=middle-1
            else:
                left=middle+1
        return [first,last]
