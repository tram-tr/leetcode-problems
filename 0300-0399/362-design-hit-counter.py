# https://leetcode.com/problems/design-hit-counter/description/

class HitCounter:
    '''
    cond: timestamp - 300 < mid
    [1, 2, 3] -> 3 @ 4
     T  T  T
    [1, 2, 3, 300] -> 4 @ 300
     T  T  T   T
    [1, 2, 3, 300] -> 3 @ 301
     F  T  T   T

    -> use binary search to find the latest hit within the past 300 seconds
    -> the number of hits = len(hits) - index of the latest hit

    [2, 3, 4] -> 3 @ 300
    [2, 3, 4] -> 3 @ 301
    [2, 3, 4] -> 2 @ 302
    [2, 3, 4] -> 1 @ 303
    [2, 3, 4] -> 0 @ 304
    '''

    def __init__(self):
        self.hits = []

    def hit(self, timestamp: int) -> None:
        self.hits.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        left = 0
        right = len(self.hits) - 1

        while left < right:
            mid = left + (right - left) // 2
            if timestamp - 300 < self.hits[mid]:
                right = mid
            else:
                left = mid + 1

        # if there is no hit within the last 300s
        if left < len(self.hits) and timestamp - 300 < self.hits[left]:
            return len(self.hits) - left
        else:
            return 0


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)
