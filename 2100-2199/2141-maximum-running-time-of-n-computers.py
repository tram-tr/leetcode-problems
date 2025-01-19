# https://leetcode.com/problems/maximum-running-time-of-n-computers/submissions/1513162490

class Solution:
    def maxRunTime(self, n: int, batteries: List[int]) -> int:
        def condition(x):
            s = 0
            for i in range(len(batteries)):
                s += min(x, batteries[i])
            return x * n <= s
        
        left = 1
        right = sum(batteries) // n

        while left < right:
            mid = right - (right - left) // 2
            if condition(mid):
                left = mid
            else:
                right = mid - 1

        return left
            
