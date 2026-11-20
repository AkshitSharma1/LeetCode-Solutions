import heapq
class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m = len(heights)
        n = len(heights[0])
        visited = set()
        heap = [(0,(0,0))] #cost,(startX,startY)
        heapq.heapify(heap)
        minDist = [[1e7]*n for _ in range(m)]
        minDist[0][0] = 0
        while heap:
            totalCostSoFar, currNode = heapq.heappop(heap)
            if currNode in visited: continue
            visited.add(currNode)
            currR,currC = currNode[0],currNode[1]
            if currR==m-1 and currC==n-1:
                return totalCostSoFar
            
            #Explore both options
            #C1 Down
            displacement = [(1,0),(0,1),(-1,0),(0,-1)]
            for dR,dC in displacement:
                newR = currR+dR
                newC = currC+dC
                if newR>=m or newC>=n or newR<0 or newC<0:
                    continue
                newCostSoFar = max(abs(heights[newR][newC]-heights[currR][currC]),
                totalCostSoFar)
                if newCostSoFar<=minDist[newR][newC]:
                    minDist[newR][newC] = newCostSoFar
                    heapq.heappush(heap,(newCostSoFar,(newR,newC)))
        return -1
            
        