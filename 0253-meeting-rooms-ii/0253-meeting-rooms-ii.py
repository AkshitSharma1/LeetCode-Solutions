class Solution:
    def minMeetingRooms(self, intervals: list[list[int]]) -> int:
        intervals.sort(key=lambda x:(x[1],x[0]))
        min_rooms = 0
        curr_room = 0
        prefix_array = defaultdict(int)
        for interval in intervals:
            prefix_array[interval[0]]+=1
            prefix_array[interval[1]]-=1
        
        for key in sorted(prefix_array.keys()):
            curr_room += prefix_array[key]
            min_rooms = max(min_rooms,curr_room)
        return min_rooms
        