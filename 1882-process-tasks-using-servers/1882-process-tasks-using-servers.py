class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available_servers = [] #() weight, index) available at current instant
        #monotonic dequeue for server (free time, weight index)
        # for each task- first offload from monotonic dequeu to available servers and put it in (weight,index)
        all_servers = sorted(
            [(0,w,i) for i,w in enumerate(servers)],
            key = lambda x:(x[1],x[2]))
        heapq.heapify(all_servers)
        answer = [-1]*(len(tasks))
        i = 0
        time = 0
        while i<len(tasks):
            time = max(time,i)
            task_time = tasks[i]
            while all_servers and all_servers[0][0]<=time:
                _,server_weight,server_index = heapq.heappop(all_servers)
                heapq.heappush(available_servers,(server_weight,server_index))
            
            if not available_servers:
                time = all_servers[0][0]
                continue
            
            server_weight,server_index = heapq.heappop(available_servers)
            #assign to this server
            answer[i] = server_index
            #push to all_servers heap
            heapq.heappush(all_servers,(time+task_time,server_weight,server_index))
            i+=1
            
        return answer
    



