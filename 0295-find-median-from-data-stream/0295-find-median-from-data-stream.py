class MedianFinder:

    def __init__(self):
        self.minHeap = []
        self.maxHeap = []
        heapq.heapify(self.minHeap)
        heapq.heapify(self.maxHeap)

        

    def addNum(self, num: int) -> None:
        heapq.heappush(self.maxHeap,-num)
        heapq.heappush(self.minHeap,-heapq.heappop(self.maxHeap))
        if len(self.minHeap)>len(self.maxHeap):
            heapq.heappush(self.maxHeap,-heapq.heappop(self.minHeap))
        
        

    def findMedian(self) -> float:
        if len(self.maxHeap) > len(self.minHeap):
            return -self.maxHeap[0]
        return (-self.maxHeap[0] + self.minHeap[0]) / 2
        
        