class Solution:
    def mostBooked(self, n: int, meetings: list[list[int]]) -> int:
        meeting_count = defaultdict(int) #contains number of meetings per room

        meetings.sort(key=lambda x:x[0])
        available_rooms = [i for i in range(n)] #min_heap, (room_number)
        occupied_rooms = [] #min_heap, (leaving time,room number))
        for start,finish in meetings:
            #firt see if any occupied room is now free or not
            while occupied_rooms and occupied_rooms[0][0]<=start:
                heapq.heappush(available_rooms,heapq.heappop(occupied_rooms)[1])
            
            #c1- room is available-> just pick the room and use it
            if len(available_rooms)>0:
                curr_room = heapq.heappop(available_rooms)
                meeting_count[curr_room]+=1
                heapq.heappush(occupied_rooms,(finish,curr_room))
            else:
                #No room is available, we must assign this meet to the room that gets free
                next_room_available_time, next_room_number = heapq.heappop(occupied_rooms)
                heapq.heappush(occupied_rooms,
                (next_room_available_time+(finish-start),next_room_number))
                meeting_count[next_room_number]+=1
        
        max_meet_count = 0
        max_room_number = -1
        for room_number,meet_count in meeting_count.items():
            if meet_count>max_meet_count:
                max_meet_count = meet_count
                max_room_number = room_number
        return max_room_number


