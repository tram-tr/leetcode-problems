# https://leetcode.com/problems/divide-chocolate/description/

class Solution:
   def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
       def condition(x):
           s = 0
           count = 0
           for i in range(len(sweetness)):
               s += sweetness[i]
               if s >= x:
                   s = 0
                   count += 1
           return count > k


       left = 0
       right = sum(sweetness)
       while left < right:
           mid = right - (right - left) // 2
           if condition(mid):
               left = mid
           else:
               right = mid - 1
       return left
