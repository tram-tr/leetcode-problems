# https://leetcode.com/problems/range-sum-query-2d-immutable/

class NumMatrix(object):

    def __init__(self, matrix):
        """
        :type matrix: List[List[int]]
        """
        n = len(matrix)
        m = len(matrix[0])
        self.prefix_sum = [[0] * m for _ in range(n)]
        
        for i in range(n):
            self.prefix_sum[i][0] = matrix[i][0]
            for j in range(1, m):
                self.prefix_sum[i][j] = self.prefix_sum[i][j-1] + matrix[i][j]

    def sumRegion(self, row1, col1, row2, col2):
        """
        :type row1: int
        :type col1: int
        :type row2: int
        :type col2: int
        :rtype: int
        """
        s = 0
        i = row1
        while i <= row2:
            if col1 != 0:
                s += self.prefix_sum[i][col2] - self.prefix_sum[i][col1 - 1]
            else:
                s += self.prefix_sum[i][col2]

            i += 1

        return s


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
