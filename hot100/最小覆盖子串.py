class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        left=0
        count_s=Counter()
        count_t=Counter(t)
        Length=float('inf')
        output=[]
        for right in range(len(s)):
            count_s[s[right]]+=1
            #统计个数
            while all(count_s[char]>=count_t[char] for char in count_t):
                #窗口
                L=right-left+1
                if L<Length:
                    Length=L
                    output=s[left:right+1]
                count_s[s[left]]-=1
                #缩小窗口
                if count_s[s[left]]==0:
                    count_s.pop(s[left])
                left+=1
        return output
