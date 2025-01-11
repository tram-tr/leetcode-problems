# https://leetcode.com/problems/spiral-matrix/description/

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = []
        while matrix:
            row = matrix.pop(0)
            m.extend(row)
            
            # transpose matrix
            matrix = list(zip(*matrix))
            # reverse row
            matrix = list(reversed(matrix))
    
        return m


