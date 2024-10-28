

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        count=0
        while count<len(s):

            s=s[:count]+s[count:count+k][::-1]+s[count+k:]
            count=count+2*k
        return s


