class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        #we reverse the group
        reversed_adj_list = defaultdict(list)
        indegree = defaultdict(int)
        n = len(graph)
        for node in range(n):
            for neighbour in graph[node]:
                reversed_adj_list[neighbour].append(node)
                indegree[node]+=1
        
        queue = deque([i for i in range(n) if indegree[i]==0])
        topological_order = []
        while queue:
            curr_node = queue.popleft()
            topological_order.append(curr_node)
            #explore all neighbours of this
            for neighbour in reversed_adj_list[curr_node]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0:
                    queue.append(neighbour)
        return sorted(topological_order)
                    #topological_order.append(neighbour)
