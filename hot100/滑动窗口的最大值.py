class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        res=[]
        que=deque() #双端队列,对头元素最大
        for i in range(len(nums)):
            while que and que[0]<i-k+1:
                que.popleft()#移除不在对头的元素
            while que and nums[que[-1]]<nums[i]:
                que.pop() #小的元素弹走
            que.append(i)
            if i>=k-1:#形成窗口
                res.append(nums[que[0]])
        return res
