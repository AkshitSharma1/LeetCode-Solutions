class Solution:
    def removeCoveredIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[0],-x[1]))
        remaining_intervals = 0
        prev_start = prev_end = float("-inf")
        for curr_start, curr_end in intervals:
            if prev_start<=curr_start and curr_end<=prev_end:
                #this interval is covered by previous interval
                #so we ignore it and continue
                continue
            else:
                #not covered by previous interval
                remaining_intervals+=1
                prev_start = curr_start
                prev_end  = curr_end
        return remaining_intervals
        