class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        meetings.sort(key=lambda x:(x[0]))
        max_end_time = meetings[0][1]
        prev_start = meetings[0][0]
        prev_end = meetings[0][1]
        free_days = 0
        for curr_start,curr_end in meetings[1:]:
            free_days += max(0,curr_start- max_end_time-1)
            max_end_time = max(max_end_time,curr_end)
        return (meetings[0][0]-1)+free_days + (days-max_end_time)



        