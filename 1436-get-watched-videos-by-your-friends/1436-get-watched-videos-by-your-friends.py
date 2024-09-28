from collections import defaultdict, deque
from typing import List

class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        watchedVideosDict = defaultdict(int)
        visited = set([id])  # Initialize with the starting person to avoid revisiting

        # BFS initialization
        queue = deque([(id, 0)])

        while queue:
            friendID, friendLevel = queue.popleft()

            # If we reach the desired level, count watched videos of this friend
            if friendLevel == level:
                for watchedVideo in watchedVideos[friendID]:
                    watchedVideosDict[watchedVideo] += 1
            # Continue the BFS only if we're below the target level
            elif friendLevel < level:
                for neighbourID in friends[friendID]:
                    if neighbourID not in visited:
                        visited.add(neighbourID)  # Mark as visited
                        queue.append((neighbourID, friendLevel + 1))

        # Sort videos by frequency first, then lexicographically by video name
        sortedVideos = sorted(watchedVideosDict.items(), key=lambda x: (x[1], x[0]))

        # Return only the video names in the sorted order
        return [video for video, _ in sortedVideos]


