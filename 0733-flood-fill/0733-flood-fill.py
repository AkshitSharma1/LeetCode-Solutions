from collections import deque
class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        m,n = len(image),len(image[0])
        queue = deque()
        visitedSet = set()
        queue.append((sr,sc))

        originalColor = image[sr][sc]
        while queue:
            currR,currC = queue.popleft()
            image[currR][currC] = color
            for dR,dC in [(0,1),(0,-1),(1,0),(-1,0)]:
                newR,newC = dR+currR, dC+currC
                if newR==-1 or newC==-1 or newR==m or newC==n: continue
                if (newR,newC) in visitedSet or image[newR][newC]!=originalColor: continue
                visitedSet.add((newR,newC))
                queue.append((newR,newC))


        return image

                


            
        