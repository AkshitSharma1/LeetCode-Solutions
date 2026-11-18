class DSU:
    def __init__(self,n):
        self.size = [1]*n
        self.parent = [i for i in range(n)]
    def findParent(self,value):
        if self.parent[value]!=value:
            self.parent[value] = self.findParent(self.parent[value])
        return self.parent[value]
    
    def union(self,a,b):
        if self.findParent(a)==self.findParent(b):
            #both have the same parents
            return False
        parent_a = self.findParent(a)
        parent_b = self.findParent(b)
        if self.size[parent_a]<self.size[parent_b]:
            parent_a, parent_b = parent_b, parent_a
        
        self.parent[parent_b] = self.parent[parent_a]
        self.size[parent_a]+=self.size[parent_b]
        return True
    

class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        dsu = DSU(len(edges)+1)
        for edge in edges:
            a,b = edge
            if dsu.union(a,b)==False:
                return edge
        return -1
        