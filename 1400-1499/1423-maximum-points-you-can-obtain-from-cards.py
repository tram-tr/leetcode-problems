# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        left = 0
        s = 0
        min_sum = float('inf')
        length = len(cardPoints) - k

        for right in range(len(cardPoints)):
            s += cardPoints[right]
            while right - left + 1 > length:
                s -= cardPoints[left]
                left += 1
            
            if right - left + 1 == length:
                min_sum = min(min_sum, s)

        return sum(cardPoints) - min_sum

