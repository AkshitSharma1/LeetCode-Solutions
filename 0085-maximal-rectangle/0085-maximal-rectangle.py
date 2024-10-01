from typing import List

class Solution:
    def calculateMaxHeight(self, heights):
        n = len(heights)
        stackLeftToRight = []
        stackRightToLeft = []
        smallerElementIndexOnLeft = [-1] * n
        smallerElementIndexOnRight = [n] * n

        for i in range(n):
            while stackLeftToRight and stackLeftToRight[-1][0] >= heights[i]:
                stackLeftToRight.pop()
            if stackLeftToRight:
                smallerElementIndexOnLeft[i] = stackLeftToRight[-1][1]
            stackLeftToRight.append((heights[i], i))

        for i in range(n - 1, -1, -1):
            while stackRightToLeft and stackRightToLeft[-1][0] >= heights[i]:
                stackRightToLeft.pop()
            if stackRightToLeft:
                smallerElementIndexOnRight[i] = stackRightToLeft[-1][1]
            stackRightToLeft.append((heights[i], i))

        ans = float('-inf')
        for i in range(n):
            ans = max(ans, (smallerElementIndexOnRight[i] - smallerElementIndexOnLeft[i] - 1) * heights[i])
        
        return ans

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        
        # Convert matrix elements to integers
        for i in range(rows):
            for j in range(cols):
                matrix[i][j] = int(matrix[i][j])
        
        # Create height matrix
        heightMatrix = [[0] * cols for _ in range(rows)]
        for j in range(cols):
            heightMatrix[0][j] = matrix[0][j]
        
        for i in range(1, rows):
            for j in range(cols):
                if matrix[i][j] == 1:
                    heightMatrix[i][j] = heightMatrix[i-1][j] + 1
                else:
                    heightMatrix[i][j] = 0
        
        # Calculate the maximum rectangle area
        ans = 0
        for row in heightMatrix:
            ans = max(ans, self.calculateMaxHeight(row))
        
        return ans
