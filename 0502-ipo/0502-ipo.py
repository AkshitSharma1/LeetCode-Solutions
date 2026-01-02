import heapq
from typing import List

class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(zip(capital, profits))  # sort by required capital
        max_heap = []
        i = 0
        n = len(projects)

        for _ in range(k):
            while i < n and projects[i][0] <= w:
                heapq.heappush(max_heap, -projects[i][1])  # max-heap via negative
                i += 1

            if not max_heap:
                break

            w += -heapq.heappop(max_heap)

        return w
