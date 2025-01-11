# https://leetcode.com/problems/squares-of-a-sorted-array/description/

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        res = []
        while left <= right:
            s_left = nums[left] * nums[left]
            s_right = nums[right] * nums[right]
            if s_left < s_right:
                res.append(s_right)
                right -= 1
            else:
                res.append(s_left)
                left += 1
        return res[::-1]
