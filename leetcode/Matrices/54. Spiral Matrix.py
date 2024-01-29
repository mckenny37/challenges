
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        x = 0
        y = -1
        maxX = len(matrix) - 1
        maxY = len(matrix[0]) - 1
        minX = 0
        minY = 0

        state = 'r';
        while minX <= maxX and minY <= maxY:
            if state == 'r':
                while y < maxY:
                    y += 1
                    result.append(matrix[x][y])
                    
                minX += 1
                state = 'd'
            elif state == 'd':
                while x < maxX:
                    x += 1
                    result.append(matrix[x][y])
            
                maxY -= 1
                state = 'l'
            
            elif state == 'l':
                while y > minY:
                    y -= 1
                    result.append(matrix[x][y])
    
                maxX -= 1
                state = 'u'

            elif state == 'u':
                while x > minX:
                    x -= 1
                    result.append(matrix[x][y])
                
                minY += 1
                state = 'r'
            
        return result

