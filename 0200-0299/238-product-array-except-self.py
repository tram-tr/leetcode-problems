# https://leetcode.com/problems/product-of-array-except-self/description/

class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        prefix_left = [1] * len(nums)
        prefix_right = [1] * len(nums)

        prefix_left[0] = nums[0]
        for i in range(1, len(nums)):
            prefix_left[i] = prefix_left[i-1] * nums[i]
        
        prefix_right[len(nums)-1] = nums[len(nums)-1]
        for i in range(len(nums)-2, 0, -1):
            prefix_right[i] = prefix_right[i+1] * nums[i]

        answer = [0] * len(nums)
        answer[0] = prefix_right[1]
        answer[len(nums)-1] = prefix_left[len(nums)-2]
        for i in range(1, len(nums)-1):
            answer[i] = prefix_left[i-1] * prefix_right[i+1]

        return answer 
        