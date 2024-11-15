class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        result=0
        g.sort()
        s.sort()#大胃口优先
        index=len(s)-1
        for i in range(len(g)-1,-1,-1):
            if index>=0 and s[index]>=g[i]:
                result+=1
                index-=1
        return result
