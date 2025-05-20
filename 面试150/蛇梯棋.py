class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n=len(board)
        def get_position(s):
            quot,rem=divmod(s-1,n) #返回商和余数
            #quot表示第几行,从下往上数
            #rem表示当前行的列偏移
            row=n-1-quot
            col=rem if (n-1-row)%2==0 else n-1-rem 
            #列号如果是偶数行(从左到右）col=rem 奇数行就n-1-rem
            return row,col
        visited=set()
        queue=deque([(1,0)])#位置,步数
        while queue:
            s,moves=queue.popleft()
            for i in range(1,7):
                next_s=s+i  #尝试走1~6步
                if next_s>n*n:
                    continue

                r,c=get_position(next_s)
                if board[r][c]!=-1:
                    next_s=board[r][c]
                if next_s==n*n: #到达终点
                    return moves+1
                if next_s not in visited:
                    visited.add(next_s)
                    queue.append((next_s,moves+1)) #加入队列
        return -1
