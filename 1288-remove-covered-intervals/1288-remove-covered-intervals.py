class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        prev_start = float("-inf")
        prev_end = float("-inf")
        remaining_interval = 0 
        for curr_start,curr_end in intervals:
            #c1. new interval covered completely by earlier
            if curr_start>=prev_start and curr_end<=prev_end:
                #remove this continue, do nothing
                continue
            elif curr_start==prev_start and curr_end>=prev_end:
                #remove this interval
                prev_end = curr_end
            else:
                remaining_interval+=1
                prev_start = curr_start
                prev_end = curr_end
                continue



        return remaining_interval
