class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
         #需要先构建树然后再DFS
        root=TrieNode()
        for word in words:
            node=root
            for char in word:
                if char not in node.children:
                    node.children[char]=TrieNode()
                node=node.children[char]
            node.word=word #到达尾部设置单词
        m,n=len(board),len(board[0])
        result=[]
        def dfs(i,j,node):
            char=board[i][j]
            if char not in node.children:
                return 
            next_node=node.children[char]
            if next_node.word:
                result.append(next_node.word)
                next_node.word=None #避免重复加入
            board[i][j]='#'
            for dx,dy in [[-1,0],[0,1],[0,-1],[1,0]]:
                x,y=i+dx,j+dy 
                if 0<=x<m and 0<=y<n and board[x][y]!='#':
                    dfs(x,y,next_node)
            board[i][j]=char #回溯
        for i in range(m):
            for j in range(n):
                dfs(i,j,root)
        return result
