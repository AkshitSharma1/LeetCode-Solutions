class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        s = ""
        max_heap = []
        heapq.heapify(max_heap)
        for char,count in [("a",a),("b",b),("c",c)]:
            if count==0: continue
            heapq.heappush(max_heap,(-count,char))
        while max_heap:
            freq, char = heapq.heappop(max_heap)
            if len(s)>=2 and s[-2]==s[-1]==char:
                #pop another
                if not max_heap: return s
                freq2, char2 = heapq.heappop(max_heap)
                s+=char2
                freq2+=1
                if freq2<0: 
                    heapq.heappush(max_heap,(freq2,char2))
            else:
                s+=char
                freq+=1
            
            if freq<0:
                heapq.heappush(max_heap,(freq,char))
        return s
            
            

