class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return 0
        n=len(triangle)
        for i in range(len(triangle)-2,-1,-1):#倒数第二层向上更新
            for j in range(len(triangle[i])):
                triangle[i][j]+=min(triangle[i+1][j],triangle[i+1][j+1])
        return triangle[0][0]
    
