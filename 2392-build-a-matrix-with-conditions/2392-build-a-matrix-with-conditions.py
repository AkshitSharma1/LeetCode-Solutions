class Solution:
    def buildMatrix(self, k: int, rowConditions: list[list[int]], colConditions: list[list[int]]) -> list[list[int]]:
        matrix = [[0]*(k) for _ in range(k)] #k*k 0 matrix
        
        def topologicalSort(conditions):
            #sorts the elements k to return a topological sort as per conditions
            adj_list = defaultdict(list)
            indegree = defaultdict(int)
            for condition in conditions:

                a,b = condition
                adj_list[a].append(b)
                indegree[b]+=1
            
            queue = deque([i for i in range(1,k+1) if indegree[i]==0])
            answer = []
            while queue:
                curr = queue.popleft()
                answer.append(curr)
                #we wil discover all neighbour
                for neighbour in adj_list[curr]:
                    indegree[neighbour]-=1
                    if indegree[neighbour]==0: queue.append(neighbour)
            return answer


        row_order = topologicalSort(rowConditions)
        col_order = topologicalSort(colConditions)
        if len(row_order)!=k or len(col_order)!=k: return []

        #recover the indexes
        #we will be using a map mapping the number to index 
        row_index = defaultdict(lambda:-1)
        col_index = defaultdict(lambda:-1)

        for i,number in enumerate(row_order): row_index[number] = i
        for i,number in enumerate(col_order): col_index[number] = i

        for number in row_order:
            matrix[row_index[number]][col_index[number]] = number

        return matrix



        