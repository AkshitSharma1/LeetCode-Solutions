class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        #sort the queries array
        n = len(queries)
        m = len(intervals)
        queries = [(q,i) for i,q in enumerate(queries)]
        queries.sort(key= lambda x:x[0])
        answer = [-1]*(n)
        intervals.sort(key=lambda x:x[0])
        min_heap = []
        intervals_index = 0
        heapq.heapify(min_heap) #(e-s,s,e)
        for query,query_index in queries:
            while intervals and intervals_index<m and intervals[intervals_index][0]<=query:
                interval_start,interval_end = intervals[intervals_index][0],intervals[intervals_index][1]
                interval_duration = interval_end-interval_start+1
                heapq.heappush(min_heap,(interval_duration,interval_start,interval_end))
                intervals_index+=1
            
            
            
            while min_heap and min_heap[0][2]<query:
                heapq.heappop(min_heap)

            if not min_heap:
                answer[query_index] = -1
                continue
            
            interval_duration,_,_ = min_heap[0]
            answer[query_index]= interval_duration
        return answer




        