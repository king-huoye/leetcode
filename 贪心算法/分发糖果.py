class Solution:
    def candy(self, ratings: List[int]) -> int:
        candys=[1]*len(ratings)
        for i in range(1,len(ratings)):
            if ratings[i]>ratings[i-1]:
                candys[i]=candys[i-1]+1
        #上面是考虑左边比右边大的
        for i in range(len(ratings)-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                candys[i]=max(candys[i],candys[i+1]+1)
        result=0
        for i in range(len(candys)):
            result+=candys[i]
        return result
        
