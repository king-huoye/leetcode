class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ''
        minLength=float('inf')
        left=0
        Counts=Counter()
        CountT=Counter(t)
        min_output=''
        for right in range(len(s)):
            Counts[s[right]]+=1
            while all(Counts[char]>=CountT[char] for char in CountT):#不能写为for char in t这样会超时
                length=right-left+1
                if length<minLength:
                    minLength=length
                    min_output=s[left:right+1]
                Counts[s[left]]-=1 #左窗口
                if Counts[s[left]]==0:
                    Counts.pop(s[left]) #删除
                left+=1
        return min_output
