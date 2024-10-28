class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False
        while '()' in s or '{}' in s or '[]' in s:
            s=s.replace('{}','')
            s=s.replace('()','')
            s=s.replace('[]','')
        if s=='':
            return True
        else:
            return False
