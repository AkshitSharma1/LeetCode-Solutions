import math
class Solution:
    def dist(self,a,b):
        return math.fabs(a-b)
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        self.maxHeap = []
        heapq.heapify(self.maxHeap)
        for num in arr:
            if len(self.maxHeap)<k:
                heapq.heappush(self.maxHeap,(-self.dist(num,x),num))
            else:
                maxDistElement = -self.maxHeap[0][0]
                if maxDistElement>self.dist(num,x) or (maxDistElement==self.dist(num,x) and num<self.maxHeap[0][1]): 
                    heapq.heappop(self.maxHeap)
                    heapq.heappush(self.maxHeap,(-self.dist(num,x),num))
        
        answer = []
        while self.maxHeap:
            answer.append(heapq.heappop(self.maxHeap)[1])
        return sorted(answer)

