from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [0]*n
        visited = set()
        for node in range(n):
            if node not in visited:
                visited.add(node)
                queue = deque()
                queue.append(node)
                maxColor = 0
                while queue:
                    currentNode = queue.popleft()
                    for neighbourNode in graph[currentNode]:
                        if neighbourNode not in visited:
                            queue.append(neighbourNode)
                            visited.add(neighbourNode)
                        if color[neighbourNode]==color[currentNode]:
                            color[neighbourNode]= color[currentNode]+1
                            if color[neighbourNode]>=2: return False
                    
        return True
        

            



        