from math import sqrt

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        minheap = []
        for x, y in points:
            distance = sqrt(x**2 + y**2)
            minheap.append([distance, x, y])
        
        heapq.heapify(minheap)
        res = []

        for i in range(k):
            distance, x, y = heapq.heappop(minheap)
            res.append([x, y])

        return res