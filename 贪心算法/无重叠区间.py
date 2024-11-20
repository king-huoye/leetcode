class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:(x[0])) #关键词排序
        count=0
        if len(intervals)==0 or len(intervals)==1:
            return 0
        for i in range(len(intervals)):
            if intervals[i][0]>=intervals[i-1][1]:
                continue
            else:
                count+=1
                intervals[i][1]=min(intervals[i][1],intervals[i-1][1])
        return count-1
