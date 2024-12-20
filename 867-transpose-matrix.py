# https://leetcode.com/problems/transpose-matrix/description/

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])

        matrix_T = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                matrix_T[i][j] = matrix[j][i]

        return matrix_T
