from collections import defaultdict
import heapq

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        adjList = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i + 1, n):
                distance = abs(points[j][1] - points[i][1]) + abs(points[j][0] - points[i][0])
                adjList[i].append((distance, j))
                adjList[j].append((distance, i))
        
        pq = [(0, 0)]  # (cost, point)
        heapq.heapify(pq)
        visited = set()
        totalCost = 0
        
        while pq:
            cost, node = heapq.heappop(pq)
            if node in visited:
                continue
            totalCost += cost
            visited.add(node)
            for neighbourCost, neighbour in adjList[node]:
                if neighbour not in visited:
                    heapq.heappush(pq, (neighbourCost, neighbour))
        
        return totalCost
