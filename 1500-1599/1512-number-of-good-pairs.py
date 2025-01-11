# https://leetcode.com/problems/number-of-good-pairs/

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hmap = {}
        count = 0
        for i in range(len(nums)):
            x = nums[i]
            if x in hmap:
                count += hmap[x]
                hmap[x] += 1
            else:
                hmap[x] = 1

        return count
        
