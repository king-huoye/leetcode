class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if not heights:
            return 0
        result=0
        n=len(heights)
        nums=[0]*(n+2)
        stack=[]
        stack.append(0)
        for i in range(1,n+1):
            nums[i]=heights[i-1]
        for i in range(len(nums)):
                    # 当新高度比栈顶对应的高度小，说明可以计算矩形面积
            while stack and nums[stack[-1]]>nums[i]:#会一直弹出去计算的
                tmp=stack[-1]
                stack.pop()
                L=i-stack[-1]-1
                H=nums[tmp]
                result=max(result,L*H)
            stack.append(i)
        return result
