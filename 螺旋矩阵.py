from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if n==1:
            return [[1]]
        nums = [[0] * n for _ in range(n)]#定义一个独立的子列表,原来的创建修改一个子列表会影响所有
        middle=n//2
        start_x=0
        start_y=0
        count=1 #从1开始算
        for offset in range(1,middle+1):#循环的次数
            for i in range(start_y,n-offset):#从左到右
                nums[start_x][i]=count
                count+=1
            #从上到下
            for i in range(start_x,n-offset):
                nums[i][n-offset]=count
                count+=1
            #从右到左x不辩
            for i in range(n-offset,start_x,-1):
                nums[n-offset][i]=count
                count+=1
            #从下到上,y不辩
            for i in range(n-offset,start_y,-1):
                nums[i][start_y]=count
                count+=1
            start_x += 1
            start_y += 1
        if n%2==1:
            nums[middle][middle]=count

        return nums
so=Solution()
print(so.generateMatrix(4))








