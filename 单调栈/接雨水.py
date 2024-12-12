class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
        s=0
        stack=[]
        stack.append(0)
        for i in range(1,len(height)):
            while stack and height[i]>height[stack[-1]]:
                middle=stack[-1]
                stack.pop()
                if stack:#栈不为空才操作
                    h=min(height[stack[-1]],height[i])-height[middle]
                    w=i-stack[-1]-1
                    s+=h*w
            stack.append(i)
        return s
