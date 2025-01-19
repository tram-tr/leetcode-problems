# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/

class Solution:
   def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
       n, m = binaryMatrix.dimensions()
       res = m
      
       for i in range(n):
           left = 0
           right = m
          
           while left < right:
               mid = left + (right - left) // 2
               if binaryMatrix.get(i, mid):
                   right = mid
               else:
                   left = mid + 1
          
           res = min(res, left)
      
       return -1 if res >= n else res
