class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        count=Counter(s)
        res=[]
        for key,val in count.items():
            if val%2==1:#寻找奇数次数的个数
                res.append(val)
        return len(res)<2
