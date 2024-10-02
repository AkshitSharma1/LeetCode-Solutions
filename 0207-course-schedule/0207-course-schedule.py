from collections import defaultdict,deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adjList = defaultdict(list)
        indegreeCount = defaultdict(int)
        for courseNo in range(numCourses): indegreeCount[courseNo]=0
        for prerequisite in prerequisites:
            adjList[prerequisite[1]].append(prerequisite[0])
            indegreeCount[prerequisite[0]]+=1
            if prerequisite[1] not in indegreeCount:
                indegreeCount[prerequisite[1]]=0
        
        pq = deque()
        for courseID, courseIndegree in indegreeCount.items():
            if courseIndegree==0:
                pq.append(courseID)
        
        toplogicalSortedList = []
        
        while pq:
            courseID = pq.popleft()
            toplogicalSortedList.append(courseID)
            for neighbourCourseID in adjList[courseID]:
                indegreeCount[neighbourCourseID]-=1
                if indegreeCount[neighbourCourseID]==0:
                    pq.append(neighbourCourseID)
        
        if len(toplogicalSortedList)==numCourses: return True
        return False

                
        
            
        