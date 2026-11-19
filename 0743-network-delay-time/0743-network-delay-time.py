class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        min_heap = [] #(min time of arrival,node)
        arrival_times = [float("inf") for i in range(n+1)] #1 to n labelled nodes
        adj_list = defaultdict(list)
        for time in times:
            u,v,w = time
            adj_list[u].append((v,w))
        arrival_times[k] = 0

        heapq.heappush(min_heap,(0,k))
        while min_heap:
            curr_dist,curr_node = heapq.heappop(min_heap)
            for neighbour_node,neighbour_dist in adj_list[curr_node]:
                if curr_dist + neighbour_dist<arrival_times[neighbour_node]:
                    arrival_times[neighbour_node] = curr_dist + neighbour_dist
                    heapq.heappush(min_heap,(arrival_times[neighbour_node],neighbour_node))
        
        for arrival_time in arrival_times[1:]:
            if arrival_time>=1e6: return -1
        
        return max(arrival_times[1:])

