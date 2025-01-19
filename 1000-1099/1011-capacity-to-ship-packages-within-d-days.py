https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def can_load(max_w):
            count = 1
            curr_w = 0
            for w in weights:
                if curr_w + w > max_w:
                    count += 1
                    curr_w = 0
                curr_w += w
            
            return count <= days
                
        left = max(weights)
        right = sum(weights)

        while left < right:
            mid = left + (right - left) // 2
            if can_load(mid):
                right = mid
            else:
                left = mid + 1

        return left
