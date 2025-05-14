class Solution:
    def intToRoman(self, num: int) -> str:
        if num<1:
            return ''
        num_to_map=[(1000,'M'),(900,'CM'),(500,'D'),(400,'CD'),(100,'C'),(90,'XC'),(50,'L'),(40,'XL'),(10,'X'),(9,'IX'),(5,'V'),(4,'IV'),(1,'I')]
        output=[]
        for key,val in num_to_map:
            while num>=key:
                num-=key
                output.append(val)
            if num==0:
                break
        return ''.join(output)
