class Solution:
    def reorganizeString(self, ss: str) -> str:
        max_heap = [(-freq,char) for char,freq in Counter(ss).items()] #(freq,char)
        heapq.heapify(max_heap)
        s = ""
        while max_heap:
            freq, char = max_heap[0]
            if len(s)>=1 and s[-1]==char:
                heapq.heappop(max_heap)
                if max_heap:
                    freq1, char1 = heapq.heappop(max_heap)
                    s+=char1
                    freq1+=1
                    if freq1<0:
                        heapq.heappush(max_heap,(freq1,char1))
                    heapq.heappush(max_heap,(freq,char))
                else:
                    return "" if len(s)!=len(ss) else s
            else:
                heapq.heappop(max_heap)
                s+=char
                freq+=1
                if freq<0:
                    heapq.heappush(max_heap,(freq,char))
        return s
        