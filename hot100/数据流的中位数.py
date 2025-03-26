class MedianFinder:

    def __init__(self):
        self.arr=list()

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        if not self.arr:
            return 0
        n=len(self.arr)
        self.arr.sort()
        if n%2==1:
            return self.arr[int(n/2)]
        else:
            return (self.arr[int(n/2)]+self.arr[int(n/2)-1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
