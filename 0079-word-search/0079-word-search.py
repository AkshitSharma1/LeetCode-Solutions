from collections import defaultdict,deque
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        #m*n
        wordLength = len(word)

        #First count frequencies and see if its even possible or not
        freqCount = defaultdict(int)
        for row in board:
            for letter in row:
                freqCount[letter]+=1
        for letter in word:
            freqCount[letter]-=1
            if freqCount[letter]<0: return False
        
        visited = [[0 for _ in range(n)] for _ in range(m)]
        def dfs(i,j,pointer):
            if pointer==wordLength: return True
            if i<0 or j<0 or i>=m or j>=n: return False
            if visited[i][j]: return False
            if word[pointer]!=board[i][j]: return False
            if word[pointer]==board[i][j]:
                visited[i][j]=1

                result = (dfs(i+1,j,pointer+1) or dfs(i,j+1,pointer+1) or dfs(i-1,j,pointer+1) or dfs(i,j-1,pointer+1))
                visited[i][j]=0
                return result
           
        
        for i in range(m):
            for j in range(n):
                    if dfs(i,j,0)==True:
                        return True
        return False
            
        
    
        