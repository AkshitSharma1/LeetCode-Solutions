class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rowBitmask = [0]*n
        colBitmask = [0]*n
        squareBitmask = [0]*n
        for rowIndex in range(n):
            for colIndex in range(n):
                val = board[rowIndex][colIndex]
                if val=='.': continue
                val = int(val)
                if rowBitmask[rowIndex] & 1<<val:
                    return False
                rowBitmask[rowIndex] |= 1<<val
                if colBitmask[colIndex] &  1<<val:
                    return False
                colBitmask[colIndex] |=  1<<val
                squareIndex = (rowIndex//3)*3+(colIndex//3)
                if squareBitmask[squareIndex] &  1<<val:
                    return False
                squareBitmask[squareIndex] |=  1<<val
        return True



        