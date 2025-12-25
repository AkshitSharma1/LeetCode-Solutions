class Solution:

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1: return 1
        degree = {k:0 for i in trust for k in i}
        for people in trust:
            degree[people[0]]-=1
            degree[people[1]]+=1
        
        for person,person_degree in degree.items():
            if person_degree==n-1: return person

        return -1
