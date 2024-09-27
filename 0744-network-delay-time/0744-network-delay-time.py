import heapq
from collections import defaultdict

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # Initialize distances to infinity for all nodes
        dist = [float("inf")] * (n + 1)
        dist[k] = 0  # Distance to the starting node is 0
        
        # Priority queue to process nodes with the shortest distance
        pq = [(0, k)]  # (distance, node)
        
        # Create adjacency list for the graph
        adjList = defaultdict(list)
        for time in times:
            u, v, w = time
            adjList[u].append((v, w))
        
        # Dijkstra's algorithm
        while pq:
            curDist, node = heapq.heappop(pq)
            
            # Skip processing if the current distance is not optimal
            if curDist > dist[node]:
                continue
            
            # Explore neighbors
            for neighbor, neighborCost in adjList[node]:
                if dist[node] + neighborCost < dist[neighbor]:
                    dist[neighbor] = dist[node] + neighborCost
                    heapq.heappush(pq, (dist[neighbor], neighbor))
        
        # Calculate the maximum time to reach all nodes
        maxDist = max(dist[1:])  # Ignore index 0 as nodes are 1-indexed
        return maxDist if maxDist != float("inf") else -1
