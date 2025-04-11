# https://leetcode.com/problems/jump-game

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        res = 0
        for i in range(len(nums)):
            if res < i:
                return False
            res = max(res, i + nums[i])

        return True
