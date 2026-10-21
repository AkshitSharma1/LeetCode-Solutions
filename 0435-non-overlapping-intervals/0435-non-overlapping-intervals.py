class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[0]))
        to_remove = 0
        prev_start = float("-inf")
        prev_end = float("-inf")
        for curr_start,curr_end in intervals:
            if curr_start>=prev_end:
                prev_end = curr_end
            else:
                #remove this interview
                to_remove+=1
        return to_remove
        