class Solution:
    def canFinish(self, numCourses: int, prerequisites: list[list[int]]) -> bool:
        n = numCourses
        indegree = defaultdict(int)
        adj_list = defaultdict(list)
        for edge in prerequisites:
            a,b = edge
            indegree[b]+=1
            adj_list[a].append(b)
        topological_sort = []
        queue = deque([i for i in range(n) if indegree[i]==0])
        while queue:
            curr_course = queue.popleft()
            topological_sort.append(curr_course)
            for neighbour in adj_list[curr_course]:
                indegree[neighbour]-=1
                if indegree[neighbour]==0: queue.append(neighbour)
        if len(topological_sort)==n: return True
        return False
        


