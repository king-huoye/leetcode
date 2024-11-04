class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        Count=Counter()#建立字典
        left=0
        Max=0
        right=0
        #右边界开始
        for right in range(len(fruits)):
            Count[fruits[right]]+=1
            while len(Count)>2:#说明此时水果种类超过2了，需要处理
                Count[fruits[left]]-=1 #处理左边界
                if Count[fruits[left]]==0:
                    Count.pop(fruits[left])
                left+=1 #更新left指针
            Max=max(Max,right-left+1)#while执行完，都要计算此时的长度
        return Max
