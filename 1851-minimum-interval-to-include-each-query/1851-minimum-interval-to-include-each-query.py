class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        queries_with_index = sorted([(q,i) for i,q in enumerate(queries)],key=lambda x:x[0])
        intervals.sort(key=lambda x:x[0])
        n = len(intervals)
        i = 0
        min_heap = [] #(length,end)
        answer = [-1]*len(queries)
        for query,index in queries_with_index:
            #Process all intervals that begin before this query
            while i<n and intervals[i][0]<=query:
                #put this to the min heap 
                heapq.heappush(min_heap,(intervals[i][1]-intervals[i][0]+1,intervals[i][1]))
                i+=1
            #remove prune expired intervals from minheap
            while min_heap and min_heap[0][1]<query:
                heapq.heappop(min_heap)
            
            #answer will be the length of this interval remaining in min heap if its ther
            answer[index] = min_heap[0][0] if min_heap else -1
        return answer
