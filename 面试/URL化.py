class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        string=list(S)
        for i in range(length):#转为列表处理
            if string[i]==' ':
                string[i]='%20'
        return ''.join(string[:length])
