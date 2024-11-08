class Solution:
    def isHappy(self, n: int) -> bool:
        result=set()#
        while n not in result:
            result.add(n)
            new_num=0
            while n:
                new_num+=(n%10)*(n%10)
                n=(int)(n/10)
            if new_num==1:
                return True
            else:
                n=new_num
        return False #说明有数字重复出现过,代表不是快乐数
