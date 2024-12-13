class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #头尾加0
        result=0
        if not heights:
            return 0
        n=len(heights)
        arr=[0]*(n+2)
        for i in range(1,n+1):
            arr[i]=heights[i-1]
        stack=[]
        stack.append(0)
        for i in range(len(arr)):
            while stack and arr[i]<arr[stack[-1]]:
                middle=stack[-1]
                stack.pop()
                Left=stack[-1]
                right=i 
                h=arr[middle]
                w=right-Left-1
                result=max(result,h*w)
            stack.append(i)
        return result



            
        
