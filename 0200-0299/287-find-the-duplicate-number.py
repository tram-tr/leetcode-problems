# https://leetcode.com/problems/find-the-duplicate-number/description/

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = slow

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        res = slow
        slow = nums[0]
        while slow != res:
            res = nums[res]
            slow = nums[slow]

        return res
