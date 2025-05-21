"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        n=len(grid)

        def isUniform(x,y,size):
            val=grid[x][y]
            for i in range(x,x+size):
                for j in range(y,y+size):
                    if grid[i][j]!=val:
                        return False,0
            return True,val
        
        def build(x,y,size):
            uniform,val=isUniform(x,y,size)
            if uniform:
                return Node(val==1,True,None,None,None,None)#val==1是一个布尔表达式
            else:
                half=size//2
                return Node(True,False,build(x,y,half),build(x,y+half,half),build(x+half,y,half),build(x+half,y+half,half))
        return build(0,0,n)
