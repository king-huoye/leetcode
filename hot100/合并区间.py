class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return [[]]
        n=len(intervals)
        intervals.sort(key=lambda x:(x[0]))
        res=[]
        res.append(intervals[0])
        for i in range(1,n):
            if intervals[i][0]>res[-1][1]:
             # 合并区间，只需要更新结果集最后一个区间的右边界，因为根据排序，左边界已经是最小的
                res.append(intervals[i])
            else:
                res[-1][1]=max(res[-1][1],intervals[i][1])
        return res
