class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        max_heap = []
        heapq.heapify(max_heap)
        for stone in stones: heapq.heappush(max_heap,-stone)
        while len(max_heap)>=2:
            s1 = -heapq.heappop(max_heap)
            s2 = -heapq.heappop(max_heap)
            if s1==s2:
                continue
            else:
                heapq.heappush(max_heap,-(s1-s2))
        if max_heap: return -max_heap[0]
        return 0

