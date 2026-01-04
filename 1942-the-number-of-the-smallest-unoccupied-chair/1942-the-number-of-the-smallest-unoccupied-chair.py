class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        times = sorted([(a,d,i) for i,(a,d) in enumerate(times)],key = lambda x:(x[0],x[1]))

        chair_count_delta = defaultdict(int)
        for arrival,departure,_ in times:
            chair_count_delta[arrival]+=1
            chair_count_delta[departure]-=1
        m = 0
        concurrent_chair_count = 0
        for time in sorted(chair_count_delta.keys()):
            concurrent_chair_count+=chair_count_delta[time]
            m = max(m,concurrent_chair_count)

        
        available_chairs = []
        busy_chairs = [(0,i) for i in range(m)] #(the time at which chair gets free, index of chair)

        i = 0
        n = len(times)
        curr_time = 0
        while i<n:
            arrival, departure,friend_index = times[i][0],times[i][1],times[i][2]
            curr_time = max(curr_time,arrival)

            while busy_chairs and busy_chairs[0][0]<=curr_time:
                _,index = heapq.heappop(busy_chairs)
                heapq.heappush(available_chairs,index)

            if not available_chairs:
                curr_time = busy_chairs[0][0]
                continue
            
            #otherwise we assign ith person the earliest chair
            chair_index = heapq.heappop(available_chairs)
            #assign to person i
            if friend_index==targetFriend: return chair_index
            heapq.heappush(busy_chairs,(curr_time+departure-arrival,chair_index))
            i+=1
        return -1

        

        
        