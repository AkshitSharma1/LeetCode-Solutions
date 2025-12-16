class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = deque([(0,"0000")])
        
        #heapq.heapify(minHeap)
        visited = set(["0000"])
        
        deadend_set = set(deadends)
        def bfs():
            while queue:
                dist, source_node = queue.popleft() 
                if source_node == target: return dist       
                if source_node in deadend_set: continue
                #We will do all variations of this node and push this in heap
                for index in range(0,4):
                    number = int(source_node[index])
                    variants = []

                    variants.append(source_node[0:index]+str((10+number-1)%10)+source_node[index+1:])
                    variants.append(source_node[0:index]+str((10+number+1)%10)+source_node[index+1:])

                    for variant in variants:
                        if variant not in deadend_set and variant not in visited:
                            queue.append((dist+1,variant))
                            visited.add(variant)
            return -1
        return bfs()                    
