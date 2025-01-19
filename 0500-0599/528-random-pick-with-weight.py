# https://leetcode.com/problems/random-pick-with-weight/

class Solution:

    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i - 1]
            
        self.w = w
        self.s = self.w[-1]
        

    def pickIndex(self) -> int:
        target = random.randint(1, self.s)
        left = 0
        right = len(self.w) - 1
        while left < right:
            mid = left + (right - left) // 2
            if target <= self.w[mid]:
                right = mid
            else:
                left = mid + 1

        return left
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
