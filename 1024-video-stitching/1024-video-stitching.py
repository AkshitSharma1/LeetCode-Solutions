class Solution:
    def videoStitching(self, clips: list[list[int]], time: int) -> int:
        max_heap = [] #store (-end, -start) 
        clips.sort(key=lambda x:x[0])
        ans = 0
        clip_index = 0
        n = len(clips)
        clips_required = 0
        t = 0
        while t<time:
            while clip_index<n and clips[clip_index][0]<=t:
                #max_heap.append(-clips[clip_index][1],-clips[clip_index][0])
                heapq.heappush(max_heap,(-clips[clip_index][1],-clips[clip_index][0]))
                clip_index+=1
            
            while max_heap and -max_heap[0][0]<=t: heapq.heappop(max_heap)
            if len(max_heap)==0: return -1
            
            clips_required+=1
            t = -max_heap[0][0]
            heapq.heappop(max_heap)
        return clips_required
        
            

            
        