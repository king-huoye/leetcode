class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result=[]
        if len(s)<4 or len(s)>12:
            return []
        def isValid(segment):
            return segment.isdigit() and 0 <= int(segment) <= 255 and (segment == "0" or not segment.startswith("0"))
        def backtracking(s,startIndex,pointSum):
            if pointSum==3:
                se=s[startIndex:]#判断最后那一部分是否符合
                if isValid(se):
                    self.result.append(s)#收集结果
                return 
            for i in range(startIndex,len(s)):
                seg=s[startIndex:i+1]
                if isValid(seg):
                    s=s[:i+1]+'.'+s[i+1:]
                    pointSum+=1
                    backtracking(s,i+2,pointSum)#因为加入了分隔符
                    s=s[:i+1]+s[i+2:]#上一步后s已经变了，下标要留意
                    pointSum-=1
        backtracking(s,0,0)
        return self.result
