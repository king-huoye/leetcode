class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix[::] = zip(*matrix[::-1])


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        new_matrix=[[0]*n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                new_matrix[j][n-i-1]=matrix[i][j]
        matrix[:]=new_matrix
