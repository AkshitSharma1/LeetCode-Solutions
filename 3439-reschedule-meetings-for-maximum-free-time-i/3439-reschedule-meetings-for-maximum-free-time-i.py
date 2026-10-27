class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gap_array = []
        prev_start = prev_end = None
        last_end_time = None
        
        for start_time,end_time in sorted(zip(startTime,endTime),key=lambda x:x[0]):
            if prev_end == None:
                gap_array.append(start_time)
            else:
                #prev end is not none so we must have had something before this
                gap_array.append(start_time-prev_end)
            last_end_time = end_time
            prev_end = end_time
            prev_start = start_time
        
        gap_array.append(eventTime-last_end_time if (eventTime-last_end_time)>0 else 0)
        #select k+1 windows from this
        l = 0
        curr_sum = 0
        max_sum = 0
        for r in range(len(gap_array)):
            curr_sum += gap_array[r]
            if r-l+1>k+1:
                curr_sum-=gap_array[l]
                l+=1
            max_sum = max(max_sum,curr_sum)

        return max_sum

        