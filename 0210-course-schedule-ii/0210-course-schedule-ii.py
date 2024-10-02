from collections import defaultdict, deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) :
        adjacency_list = defaultdict(list)
        indegree_count = defaultdict(int)
        
        for course in range(numCourses):
            indegree_count[course] = 0
        
        for prerequisite in prerequisites:
            next_course, prev_course = prerequisite
            adjacency_list[prev_course].append(next_course)
            indegree_count[next_course] += 1
            if prev_course not in indegree_count:
                indegree_count[prev_course] = 0
        
        zero_indegree_queue = deque()
        for course, indegree in indegree_count.items():
            if indegree == 0:
                zero_indegree_queue.append(course)
        
        topological_sorted_list = []
        
        while zero_indegree_queue:
            course = zero_indegree_queue.popleft()
            topological_sorted_list.append(course)
            for neighbor in adjacency_list[course]:
                indegree_count[neighbor] -= 1
                if indegree_count[neighbor] == 0:
                    zero_indegree_queue.append(neighbor)
        
        if len(topological_sorted_list) ==numCourses:
            return topological_sorted_list
        return []
