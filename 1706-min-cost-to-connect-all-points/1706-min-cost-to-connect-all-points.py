import heapq
class Solution:

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        visited = set()
        heap = [(0,0,0)] #(weight,source node, and the destination of edge)
        cost = 0
        minCost = [1e7]*n
        minCost[0] = 0
        heapq.heapify(heap)
        while heap:
            weight,sourceNode,neighbourNode = heapq.heappop(heap)
            if neighbourNode not in visited:
                visited.add(neighbourNode)
            
            for nextNode in range(n):
                if nextNode in visited: continue
                cost = abs(points[nextNode][0]-points[neighbourNode][0])+abs(points[nextNode][1]-points[neighbourNode][1])
                if cost<minCost[nextNode]:
                    minCost[nextNode] = cost
                    heapq.heappush(heap,(cost,neighbourNode,nextNode))
            
        return sum(minCost)

        