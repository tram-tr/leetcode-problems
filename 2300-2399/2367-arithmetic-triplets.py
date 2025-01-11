# https://leetcode.com/problems/number-of-arithmetic-triplets/description/

class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        check = set()
        count = 0
        
        # z - y = d => y = z - d
        # y - x = d => x = y - d = z - 2d
        for i in range(len(nums)):
            z = nums[i]
            y = z - diff
            x = z - 2 * diff
            if (x >= 0 and x in check) and (y >= 0 and y in check):
                count += 1
            check.add(z)

        return count 
