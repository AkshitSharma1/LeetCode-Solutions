class Solution:
    def minCostConnectPoints(self, points: list[list[int]]) -> int:
        #Prims algorithm using min heap
        adj_list = defaultdict(list)
        n = len(points)
        for i in range(n):
            for j in range(i+1,n):
                adj_list[i].append((j,abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])))
                adj_list[j].append((i,abs(points[i][0]-points[j][0])+abs(points[i][1]-points[j][1])))
        
        #prims algorithm
        min_heap = [(0,0,-1)] #cost of edge,point_index,parent_index
        min_cost = 0
        in_tree = defaultdict(lambda:False)
        while min_heap:
            cost,curr,parent = heapq.heappop(min_heap)
            if in_tree[curr]: continue
            in_tree[curr] = True
            if parent!=-1:
                min_cost+=cost
            for neighbour,neighbour_cost in adj_list[curr]:
                if in_tree[neighbour]==False:
                    heapq.heappush(min_heap,(neighbour_cost,neighbour,curr))
        return min_cost


