class DSU:
    def __init__(self,n):
        self.size = [1]*n
        self.parent = list(range(n))
    
    def find(self,a):
        if self.parent[a]==a: return a
        self.parent[a] = self.find(self.parent[a])
        return self.parent[a]
    
    def union(self,a,b):
        parent_a = self.find(a)
        parent_b = self.find(b)
        if parent_a==parent_b:
            return False
        if self.size[parent_a]<self.size[parent_b]:
            parent_a,parent_b = parent_b,parent_a
        
        self.parent[parent_b] = parent_a
        self.size[parent_a] += self.size[parent_b]
        return True
    

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        n = len(edges)
        dsu = DSU(n+1)
        for edge in edges:
            a,b = edge
            if dsu.union(a,b)==False:
                return edge
        return -1
        
        