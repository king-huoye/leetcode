class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        five=0
        ten=0
        twenty=0
        for i in bills:
            if i==5:
                five+=1
            elif i==10:
                if five==0:
                    return False
                ten+=1
                five-=1
            elif i==20:
                if ten>0 and five>0:
                    five-=1
                    ten-=1
                elif five>=3:
                    five-=3
                else:
                    return False
        return True
  ## 
  class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        count={5:0,10:0,20:0}
        for bill in bills:
            if bill==5:
                count[5]+=1
            elif bill==10:
                if count[5]<=0:
                    return False
                count[10]+=1
                count[5]-=1
            elif bill==20:
                if count[5]>0 and count[10]>0:
                    count[5]-=1
                    count[10]-=1
                elif count[5]>=3:
                    count[5]-=3
                else:
                    return False
        return True
        
