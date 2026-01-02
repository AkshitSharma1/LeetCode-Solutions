class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        task_frequency = Counter(tasks)
        task_names = task_frequency.keys()
        answer = []
        queue = deque() #will contain [next_execution_time,frequency,task]
        max_heap =[]
        heapq.heapify(max_heap)

        for task in task_names:
            queue.append((0,task_frequency[task],task))
        del task_frequency
        del task_names
        del answer
        #max frequency heap via (task_frequency,task)
        time = 0
        while queue or max_heap:
            while queue and queue[0][0]<=time:
                execution_time,frequency,task =  queue.popleft()
                heapq.heappush(max_heap,(-frequency,execution_time,task))
            
            if len(max_heap)==0:
                #No time to run at this time
            
                time = queue[0][0]

                continue
            frequency,execution_time,task = heapq.heappop(max_heap)
            frequency = -frequency
            frequency-=1
            if frequency>0:
                queue.append((time+n+1,frequency,task))
            time+=1
        return time


            