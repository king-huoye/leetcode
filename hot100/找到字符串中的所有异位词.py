class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if not p and len(s)<len(p):
            return []
        res=[]
        count_p=[0]*26
        count_s=[0]*26
        for i in range(len(p)):
            count_p[ord(p[i])-ord('a')]+=1 #统计p的个数
        left=0
        for right in range(len(s)):
            count_s[ord(s[right])-ord('a')]+=1

            #窗口缩小
            if right>=len(p):
                char_left=s[left] #左窗口要回缩
                count_s[ord(char_left)-ord('a')]-=1
                left+=1
            if count_p==count_s:
                res.append(left)
        return res
