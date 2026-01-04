class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #n tasks
        #each task- [enquietime i, processtinjg time p]
        queue = deque(sorted([(e,p,i) for i,(e,p) in enumerate(tasks)]
            ,key=lambda x:(x[0],x[1],x[2]))
        )
        min_heap = [] #([processing time, index])
        time = 0
        answer = []
        while queue or min_heap:
            while queue and queue[0][0]<=time:
                e,p,i = queue.popleft()
                heapq.heappush(min_heap,(p,i))
            
            if not min_heap:
                time = queue[0][0] 
                continue
            
            p,i = heapq.heappop(min_heap)
            answer.append(i)
            time+=p
        
        return answer