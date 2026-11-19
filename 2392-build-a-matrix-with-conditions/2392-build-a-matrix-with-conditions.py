class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        def topologicalSort(conditions):
            nonlocal k
            topological_sort = []
            adj_list = defaultdict(list)
            indegree = defaultdict(int)
            for edge in conditions:
                a,b  = edge
                adj_list[a].append(b)
                indegree[b]+=1
            queue = deque([i for i in range(1,k+1) if indegree[i]==0])
            while queue:
                curr = queue.popleft()
                topological_sort.append(curr)
                for neighbour in adj_list[curr]:
                    indegree[neighbour]-=1
                    if indegree[neighbour]==0:
                        queue.append(neighbour)
            return topological_sort

        row_topological_order = topologicalSort(rowConditions)
        col_topological_order = topologicalSort(colConditions)
        if len(row_topological_order)<k or len(col_topological_order)<k: return []

        #now form from these we form the matrix
        row_index = defaultdict(int) #maps number to row index
        col_index = defaultdict(int) #maps the number to col index
        for i,number in enumerate(row_topological_order): row_index[number] = i
        for i,number in enumerate(col_topological_order): col_index[number] = i
        matrix = [[0]*k for _ in range(k)]
        for number in col_topological_order:
            matrix[row_index[number]][col_index[number]] = number
        return matrix



                
            

            
        