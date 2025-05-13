class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if not citations:
            return 0
        n=len(citations)
        citations.sort()
        for i in range(n):
            h=n-i #记录当前论文到末尾论文的潜在h指数
            if citations[i]>=h:
                return h 
        return 0
            
