class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        busy = [(0,i) for i in range(n)] #(end time, index)
        available = [] # (index)
        heapq.heapify(busy)
        heapq.heapify(available)
        meetings.sort(key=lambda x:x[0])
        m = len(meetings)

        freq_count = defaultdict(int)
        
        
        i = 0
        time = 0
        while i<m:
            curr_start,curr_end = meetings[i][0],meetings[i][1]
            if curr_start>time:
                time = curr_start
                continue
            while busy and busy[0][0]<=time:
                _,index = heapq.heappop(busy)
                heapq.heappush(available,index)

            if not available:
                time =busy[0][0]
                continue
            available_room = heapq.heappop(available)
            #now add to busy queue
            heapq.heappush(busy,(time+(curr_end-curr_start),available_room))
            freq_count[available_room]+=1
            i+=1
        
        max_freq = 0
        max_freq_room = 0
        for room_no, frequency in sorted(freq_count.items(),key=lambda x:x[0]):
            if frequency>max_freq:
                max_freq = frequency
                max_freq_room = room_no
        return max_freq_room       
            


