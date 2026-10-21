class Solution:
    def findMinArrowShots(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],x[1]))
        if len(intervals)<=1: return len(intervals)
        n = len(intervals)
        arrow_count = 0
        curr_start = float("inf")
        curr_end = float("inf")
        for r in range(0,n):
            if r<n and intervals[r][0]<=curr_end:
                curr_end = min(intervals[r][1],curr_end)
                curr_start = min(intervals[r][0],curr_end)
                continue
            else:
                arrow_count+=1
                curr_start = intervals[r][0]
                curr_end = intervals[r][1]
        arrow_count+=1
        return arrow_count

            
