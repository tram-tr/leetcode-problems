# https://leetcode.com/problems/find-pivot-index/description/

class Solution(object):
    def pivotIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if sum(nums[1:]) == 0:
            return 0

        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] + nums[i]

        for i in range(1, len(nums)):
            left = prefix[i-1]
            right = prefix[len(nums)-1] - prefix[i]
            if left == right:
                return i

        if sum(nums[0:-1]) == 0:
            return len(nums)-1

        return -1