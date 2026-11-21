class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        #pseudocode idea
        #adj_list
        #min_heap (0,)
        adj_list = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                dist = abs(points[j][1]-points[i][1]) + abs(points[j][0]-points[i][0])
                adj_list[i].append((j,dist))
                adj_list[j].append((i,dist))
        
        min_heap = []
        heapq.heappush(min_heap,(0,0,-1)) #cost,index,parent index
        total_cost = 0
        seen = set()
        while min_heap:
            edge_cost, curr,parent = heapq.heappop(min_heap)
            if curr in seen: continue
            seen.add(curr)
            if parent!=-1: total_cost+= edge_cost
            #we explore all neighbours
            for neighbour,edge_cost in adj_list[curr]:
                if neighbour in seen: continue
                heapq.heappush(min_heap,(edge_cost,neighbour,curr))
        return total_cost
        


        
        