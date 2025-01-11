class Solution:
    def compressString(self, s: str) -> str:
        if not s:
            return ''
        res=[]
        count=1 #需要统计相同的个数
        for i in range(1,len(s)):
            if s[i]==s[i-1]:
                count+=1
            else:
                res.append(s[i-1]+str(count))#每次添加把字符和次数以str类型进行假如
                count=1 #重新设置
        res.append(s[-1]+str(count))
        compress=''.join(res)
        return compress if len(compress)<len(s) else s
            
