# https://leetcode.com/problems/single-element-in-a-sorted-array/description/

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2
            if mid % 2 == 1:
                mid -= 1
            
            if nums[mid] != nums[mid + 1]:
                right = mid
            else:
                left = mid + 2

        return nums[left]
