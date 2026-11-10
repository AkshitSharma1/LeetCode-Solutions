class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        prev_start = prev_end = float("-inf")
        intervals.sort(key=lambda x:x[0])
        removed_intervals = 0
        for curr_start,curr_end in intervals:
            #if this current interval is covered by the previous interval
            if curr_end<=prev_end:
                #remove this curr interval
                removed_intervals+=1
                continue
            
            #if this current interval covers the previous interval, only if prev_start==curr_start and curr_end>=prev_end
            if prev_start==curr_start and curr_end>=prev_end:
                #remove the previous interval
                removed_intervals+=1
                #this curr interval now becomes prev internal for next one
                prev_start = curr_start
                prev_end = curr_end
                continue
            #no overlap
            prev_start = curr_start
            prev_end = curr_end
        return len(intervals)-removed_intervals

        