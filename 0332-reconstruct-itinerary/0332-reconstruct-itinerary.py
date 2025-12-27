class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj_list = defaultdict(list)
        for src,dest in tickets: adj_list[src].append(dest)
        for key in adj_list.keys(): adj_list[key].sort(reverse=True)
        path = []
        def dfs(node):
            while adj_list[node]:
                dfs(adj_list[node].pop())
            path.append(node)
        dfs("JFK")
        return path[::-1]
        