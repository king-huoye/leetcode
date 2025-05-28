class Solution:
    def romanToInt(self, s: str) -> int:
        if not s:
            return 0
        map_to_num={'I':1,'V':5,"X":10,'L':50,'C':100,'D':500,'M':1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        num=0
        n=len(s)
        for i in range(n-1):
            if map_to_num[s[i]]<map_to_num[s[i+1]]:
                num-=map_to_num[s[i]]
            else:
                num+=map_to_num[s[i]]
        return num+map_to_num[s[-1]]
