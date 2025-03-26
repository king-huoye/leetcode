class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        if not s:
            return []
        left=0
        right=0
        count=[0]*26
        for i in range(len(s)):
            count[ord(s[i])-ord('a')]=i
        res=[]
        for i in range(len(s)):
            right=max(right,count[ord(s[i])-ord('a')])#最大的
            if i==right:
                #收集结果
                res.append(right-left+1)
                left=right+1
        return res
