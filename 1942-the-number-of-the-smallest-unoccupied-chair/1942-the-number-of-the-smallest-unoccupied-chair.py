import heapq

class Solution:
    def smallestChair(self, times: list[list[int]], targetFriend: int) -> int:

        times_with_index = sorted(
            [[arrival, leaving, friend_index]
             for friend_index, (arrival, leaving) in enumerate(times)],
            key=lambda x: x[0]
        )

        occupied_chairs_min_heap = []  # (leaving_time, chair)
        available_chairs_min_heap = []  # chair_number

        for arrival, leaving, friend_index in times_with_index:

            if len(occupied_chairs_min_heap) == 0:
                if friend_index == targetFriend:
                    return 0
                heapq.heappush(occupied_chairs_min_heap, (leaving, 0))
                continue

            while (occupied_chairs_min_heap
                   and occupied_chairs_min_heap[0][0] <= arrival):
                heapq.heappush(
                    available_chairs_min_heap,
                    heapq.heappop(occupied_chairs_min_heap)[1]
                )

            if len(available_chairs_min_heap) == 0:
                chair = len(occupied_chairs_min_heap)

                if friend_index == targetFriend:
                    return chair

                heapq.heappush(occupied_chairs_min_heap, (leaving, chair))

            else:
                chair = heapq.heappop(available_chairs_min_heap)

                if friend_index == targetFriend:
                    return chair

                heapq.heappush(occupied_chairs_min_heap, (leaving, chair))

        return -1