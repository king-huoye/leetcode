class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        l1=[0]*26 #统计数组
        for i in range(len(s)):
            l1[ord(s[i])-ord('a')]+=1
        for i in range(len(t)):
            l1[ord(t[i])-ord('a')]-=1
        for i in range(len(l1)):
            if l1[i]!=0:
                return False
        return True
