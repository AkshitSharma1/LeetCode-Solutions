class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        queue = deque(sorted([(c,p) for c,p in zip(capital,profits)],key=lambda x:(x[0],-x[1])))
        max_heap = [] #(profit,capital)
        pick_count = 0
        while queue or max_heap:
            while queue and queue[0][0]<=w:
                cost,profit = queue.popleft()
                heapq.heappush(max_heap,(-profit,-cost))
            
            if  len(max_heap)==0: return w

            profit, cost = heapq.heappop(max_heap)
            profit *=-1
            cost *=-1 
            pick_count+=1
            w += profit
            if pick_count==k: return w
        return w

