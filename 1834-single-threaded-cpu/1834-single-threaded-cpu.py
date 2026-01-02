class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        #[[enquietime, processingtime]]
        queue = deque(sorted([(e,p,i) for i,(e,p) in enumerate(tasks)],key=lambda x:(x[0],x[1],x[2])))
        min_heap = []
        curr_time = 0
        answer = []
        while min_heap or queue:
            while queue and queue[0][0]<=curr_time:
                e,p,i = queue.popleft()
                heapq.heappush(min_heap,(p,i))
            if min_heap:
                processing_time, index = heapq.heappop(min_heap)
                curr_time += processing_time
                answer.append(index)
            else:
                curr_time = queue[0][0]
                continue
        return answer
