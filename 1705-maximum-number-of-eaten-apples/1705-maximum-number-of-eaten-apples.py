class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        max_apples_eaten = 0
        queue = []
        for i in range(len(apples)):
            if apples[i]==0: continue
            queue.append((apples[i],i,i+days[i]-1))
        queue.sort(key=lambda x:(x[1],x[2]))
        queue = deque(queue)
        min_heap = [] #(end,-apple count)
        curr_day = 0
        while queue or min_heap:
            while queue and queue[0][1]<=curr_day:
                apple_count,start_date,end_date = queue.popleft()
                heapq.heappush(min_heap,(end_date,-apple_count))
            
            
            while min_heap and min_heap[0][0]<curr_day:
                heapq.heappop(min_heap)
            if not min_heap and not queue: return max_apples_eaten
            if not min_heap:
                curr_day = queue[0][1]
                continue
            
            end_date, apple_count = heapq.heappop(min_heap)
            apple_count+=1
            max_apples_eaten+=1
            if apple_count<0:
                heapq.heappush(min_heap,(end_date,apple_count))
            curr_day+=1
        return max_apples_eaten

        
            


