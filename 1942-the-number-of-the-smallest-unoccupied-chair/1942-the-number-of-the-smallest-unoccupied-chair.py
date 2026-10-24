class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:

        times_with_index = sorted([[arrival,leave,index] for index,(arrival,leave) in enumerate(times)],key=lambda x:(x[0],x[1]))
        #we can make use of min heap
        #minheap we can store (leave time,index of friend, chair number)
        min_heap = []
        empty_chairs_min_heap = []
        for arrival,departure,friend_index in times_with_index:
            if len(min_heap)==0:
                    heapq.heappush(min_heap,(departure,friend_index,0))
                    if friend_index==targetFriend: return 0
                    continue
            while min_heap and min_heap[0][0]<=arrival:
                heapq.heappush(empty_chairs_min_heap,heapq.heappop(min_heap)[2])
           
            new_chair_index = len(min_heap) if len(empty_chairs_min_heap)==0 else heapq.heappop(empty_chairs_min_heap)

            if friend_index==targetFriend: return new_chair_index
            heapq.heappush(min_heap,(departure,friend_index,new_chair_index))
        return -1