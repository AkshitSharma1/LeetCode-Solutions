class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        events = []
        for curr_start,curr_end in intervals:
            events.append((curr_start,+1))
            events.append((curr_end,-1))
        events.sort(key=lambda x:(x[0],-x[1]))
        concurrent_intervals = 0
        ans = 0
        for timestamp,value in events:
            concurrent_intervals+=value
            ans = max(ans,concurrent_intervals)
        return ans
