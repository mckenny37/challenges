class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        def transpose(matrix):
            for col in range(len(matrix[0])):
                for row in range(col, len(matrix)):
                    matrix[col][row], matrix[row][col] = matrix[row][col], matrix[col][row]

        def reverse_rows(matrix):
            for row in range(len(matrix)):
                left = 0
                right = len(matrix)-1
                while left < right:
                    matrix[row][left], matrix[row][right] = matrix[row][right], matrix[row][left]
                    left += 1
                    right -=1
        
        transpose(matrix)
        reverse_rows(matrix)