class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        insertion_pos = bisect_left(intervals,newInterval[0],key=lambda x:x[0])
        ans = intervals[:insertion_pos]
        #if they overlap, merge them
        curr_start,curr_end = newInterval
        if ans and curr_start<=ans[-1][1]:
            ans[-1][1] = max(ans[-1][1],curr_end)
        else:
            ans.append([curr_start,curr_end])

        for interval in intervals[insertion_pos:]:
            if interval[0]<=ans[-1][1]:
                ans[-1][1] = max(ans[-1][1],interval[1])
            else:
                ans.append(interval)
            

        return ans