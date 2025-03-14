class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        #记录行和列
        row=set()
        col=set()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
        #记录0所在行和所在列
        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j]=0
        
