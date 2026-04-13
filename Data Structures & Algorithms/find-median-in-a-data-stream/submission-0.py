class MedianFinder:

    def __init__(self):
        self.smallheap = []
        self.largeheap = []

    def addNum(self, num: int) -> None:
        if abs(len(self.smallheap) + 1 - len(self.largeheap)) > 1:
            small = heapq.heappop_max(self.smallheap)
            heapq.heappush(self.largeheap, small)
            heapq.heappush_max(self.smallheap, num)
        else:
            heapq.heappush_max(self.smallheap, num)

        if self.smallheap and self.largeheap:
            while (self.smallheap[0] > self.largeheap[0]):
                small = heapq.heappop_max(self.smallheap)
                large = heapq.heapreplace(self.largeheap, small)
                heapq.heappush_max(self.smallheap, large)


    def findMedian(self) -> float:
        if len(self.smallheap) > len(self.largeheap):
            return self.smallheap[0]
        elif len(self.smallheap) < len(self.largeheap):
            return self.largeheap[0]
        else:
            return (self.smallheap[0] + self.largeheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()