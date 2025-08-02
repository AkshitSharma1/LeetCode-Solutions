class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        matrix = [list(map(int, row)) for row in matrix]

        n = len(matrix[0])
        heights = [0] * n
        maxAnswer = 0
        for m in range(len(matrix)):
            for j in range(n):
                if matrix[m][j] == 1:
                    heights[j] += 1
                else:
                    heights[j] = 0
            NSL = [-1]*n
            NSR = [n]*n
            NSLStack = []
            NSRStack = []
            #First- next smallest neighbour to right (monotonically increasing stack)
            for index in range(n-1,-1,-1):
                while NSRStack and heights[NSRStack[-1]]>=heights[index]:
                    NSRStack.pop()
                if len(NSRStack)>0:
                    NSR[index] = NSRStack[-1]
                NSRStack.append(index)


            for index in range(0,n,+1):
                while NSLStack and heights[NSLStack[-1]]>=heights[index]:
                    NSLStack.pop()
                if len(NSLStack)>0:
                    NSL[index] = NSLStack[-1]
                NSLStack.append(index)
            
            for index,number in enumerate(heights):
                maxAnswer = max(maxAnswer,int(number)*(NSR[index]-NSL[index]-1))

            
        return maxAnswer