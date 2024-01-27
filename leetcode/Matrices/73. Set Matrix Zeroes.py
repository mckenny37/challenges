class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        zeroRows = {}
        zeroColumns = {}

        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if matrix[x][y] == 0:
                    zeroColumns[x] = True
                    zeroRows[y] = True
        
        
        for x in range(len(matrix)):
            for y in range(len(matrix[x])):
                if x in zeroColumns or y in zeroRows:
                    matrix[x][y] = 0

        
        