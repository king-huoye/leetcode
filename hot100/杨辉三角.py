class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res=[]
        for i in range(numRows):
            cur_row=[1]*(i+1)#在循环里面初始化dp
            for col in range(1,i):
                cur_row[col]=res[i-1][col-1]+res[i-1][col]
            res.append(cur_row)
        return res
