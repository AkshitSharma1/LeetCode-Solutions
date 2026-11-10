class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        prev_end = float("-inf")
        removed_intervals = 0
        intervals.sort(key=lambda x:(x[1],x[0]))
        for curr_start,curr_end in intervals:
            if curr_start>=prev_end:
                #no overlap
                prev_end = curr_end
            else:
                #therer is overlap-> so we remove this interval
                removed_intervals+=1
        return removed_intervals
    

