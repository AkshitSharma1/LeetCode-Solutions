class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        maxHeap = []
        heapq.heapify(maxHeap)
        for num in arr:
            dist = abs(x-num)
            if len(maxHeap)==k:
                if dist<-maxHeap[0][0]:
                    heapq.heappop(maxHeap)
                    heapq.heappush(maxHeap,(-dist,num))
            else:
                heapq.heappush(maxHeap,(-dist,num))
        ans=[]
        while len(maxHeap)>0:
            ans.append(heapq.heappop(maxHeap)[1])
        return sorted(ans)

        