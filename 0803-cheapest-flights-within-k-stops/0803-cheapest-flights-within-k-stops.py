from typing import List

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        INF = 10**15
        dist = [INF] * n
        dist[src] = 0

        # At most k stops => at most k+1 edges
        for _ in range(k + 1):
            nextDist = dist[:]  # freeze previous layer; prevents > (current edges) chaining
            changed = False
            for u, v, w in flights:
                if dist[u] != INF and dist[u] + w < nextDist[v]:
                    nextDist[v] = dist[u] + w
                    changed = True
            dist = nextDist
            if not changed:  # early exit if no improvement
                break

        return -1 if dist[dst] == INF else dist[dst]
