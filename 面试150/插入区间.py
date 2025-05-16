class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result=[]
        #先插入在排序,在进行合并
        intervals.append(newInterval)
        intervals.sort(key=lambda x:(x[0]))
        result.append(intervals[0])
        n=len(intervals)
        for i in range(1,n):
            if intervals[i][0]>result[-1][1]:
                result.append(intervals[i])
            else:
                result[-1][1]=max(intervals[i][1],result[-1][1])

        return result
