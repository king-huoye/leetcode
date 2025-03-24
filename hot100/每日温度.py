class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []
        result=[0]*len(temperatures)
        stack=[]
        stack.append(0)
        for i in range(1,len(temperatures)):
            while stack and temperatures[stack[-1]]<temperatures[i]:#保证栈是单调递减的
                result[stack[-1]]=i-stack[-1]
                stack.pop()
            stack.append(i)
        return result
