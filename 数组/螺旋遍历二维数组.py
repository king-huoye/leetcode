class Solution:
    def spiralArray(self, array: List[List[int]]) -> List[int]:
        if len(array)==0:
            return []
        result=[]
        left,right,top,bottom=0,len(array[0])-1,0,len(array)-1
        while left<=right and top<=bottom:
            #从左到右
            for i in range(left,right+1):
                result.append(array[top][i])
            top+=1

            #从上到下
            for i in range(top,bottom+1):
                result.append(array[i][right])
            right-=1

            if top<=bottom:#为了防止重复遍历,从右到左
                for i in range(right,left-1,-1):
                    result.append(array[bottom][i])
            bottom-=1
            if left<=right:#从下到上
                for i in range(bottom,top-1,-1):
                    result.append(array[i][left])
            left+=1
        return result
            
