# https://leetcode.com/problems/koko-eating-bananas/description/

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat(speed):
            s = 0
            for i in range(len(piles)):
                s += piles[i] // speed
                if piles[i] % speed:
                    s += 1
            return s <= h

        left = 1
        right = max(piles)
        while left < right:
            mid = left + (right - left) // 2
            if can_eat(mid):
                right = mid
            else:
                left = mid + 1    

        return left
