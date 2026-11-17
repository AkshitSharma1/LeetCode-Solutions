class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        adj= defaultdict(list)
        def buildGraph(rooms):
            for curr_room,allowed_rooms in enumerate(rooms):
                adj[curr_room].extend(allowed_rooms)
        
        visited = set()
        def dfs(room):
            nonlocal visited, adj
            if room in visited: return
            visited.add(room)
            for neighbour_rooms in adj[room]:
                dfs(neighbour_rooms)
            return
        
        buildGraph(rooms)
        dfs(0)
        if len(visited)==len(rooms): return True
        return False
            
