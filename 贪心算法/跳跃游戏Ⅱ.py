class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums)==1 :
            return 0
        cover=0 #当前能覆盖最远
        next_cover=0 #下一步能覆盖的最远距离
        count=0
        for i in range(len(nums)):
            next_cover=max(i+nums[i],next_cover)
            if i==cover:#i来到当前覆盖范围的时候,此时还没到终点
                count+=1 #此时还没到终点的时候
                cover=next_cover
            if cover>=len(nums)-1:
                return count #立刻返回
