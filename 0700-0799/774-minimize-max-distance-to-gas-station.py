# https://leetcode.com/problems/minimize-max-distance-to-gas-station

class Solution:
   def minmaxGasDist(self, stations: List[int], k: int) -> float:
       def condition(x):
           count = 0


           for i in range(1, len(stations)):
               d = stations[i] - stations[i - 1]
               count += (d - 1) // x


               if count > k:
                   return False


           return count <= k
      
       left = 0
       right = 1e8
      
       while right - left > 1e-6:
           mid = left + (right - left) / 2
           if condition(mid):
               right = mid
           else:
               left = mid
      
       return left

