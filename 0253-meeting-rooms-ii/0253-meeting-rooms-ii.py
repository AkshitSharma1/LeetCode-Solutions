"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals) -> int:
        intervals.sort(key=lambda x: x[0])
        min_heap = []
        answer = 0
        for interval in intervals:
            while  min_heap and min_heap[0] <= interval[0]:
                heapq.heappop(min_heap)
            heapq.heappush(min_heap, interval[1])
            answer = max(len(min_heap),answer)

        return answer