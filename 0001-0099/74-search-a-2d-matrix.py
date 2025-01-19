# https://leetcode.com/problems/search-a-2d-matrix/description/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        m = len(matrix[0])

        left = 0
        right = n * m - 1

        while left < right:
            mid = left + (right - left) // 2
            mid_val = matrix[mid // m][mid % m]

            if mid_val >= target:
                right = mid
            else:
                left = mid + 1

        return matrix[left // m][left % m] == target
