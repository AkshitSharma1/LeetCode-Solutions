"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        min_heap = []
        for intervals in schedule:
            for interval in intervals:
                heapq.heappush(min_heap,[interval.start,interval.end])
        free_time = []
        prev_start,prev_end = heapq.heappop(min_heap)
        while min_heap:
            curr_start,curr_end = heapq.heappop(min_heap)
            #c1- no overlap-> free time
            if curr_start>prev_end:
                free_time.append(Interval(prev_end,curr_start))
                prev_end = curr_end
            else:
                #there is overlap
                prev_end = max(prev_end,curr_end)
        return free_time



        