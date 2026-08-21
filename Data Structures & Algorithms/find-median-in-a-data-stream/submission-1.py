class MedianFinder:

    def __init__(self):
        self.small = [] #maxHeap
        self.large = [] #minHeap

    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -num)

        #make sure every num in small is <= every num in large
        if self.small and self.large and ((-1*self.small[0]) > self.large[0]):
            val = -1*heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #uneven size?
        if len(self.small) > len(self.large) + 1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        if len(self.small) + 1 < len(self.large):
            val = heapq.heappop(self.large)
            heapq.heappush(self.small, -val) 

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        elif len(self.large) > len(self.small):
            return self.large[0]
        return (-1*self.small[0] + self.large[0]) / 2

        