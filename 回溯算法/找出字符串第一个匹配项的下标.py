class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getNext(next,s):
            j=0
            next[0]=0
            for i in range(1,len(s)):
                while j>0 and s[i]!=s[j]:
                    j=next[j-1]
                if s[i]==s[j]:
                    j+=1
                next[i]=j
        next=[0]*len(needle)
        j=0
        getNext(next,needle)
        for i in range(len(haystack)):
            while j>0 and haystack[i]!=needle[j]:
                j=next[j-1]
            if haystack[i]==needle[j]:
                j+=1
            if j==len(needle):
                return i-j+1
        return -1
      #return haystack.find(needle) 调库
