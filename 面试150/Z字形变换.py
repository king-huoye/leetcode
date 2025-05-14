class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s:
            return ''
        if numRows==1:
            return s
        res,n=['']*numRows,2*numRows-2 #n为Z字型变换的周期,向下有numRows个字符,向上有numRows-2个字符
        for i,c in enumerate(s):
        
            res[min(idx:=i%n,n-idx)]+=c 
        return ''.join(res)
