# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
            
        left = 0
        right = len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1
        
        start = left if nums[left] == target else -1

        left = 0
        right = len(nums) - 1
        while left < right:
            mid = right - (right - left) // 2
            if nums[mid] <= target:
                left = mid
            else:
                right = mid - 1
        
        end = right if nums[right] == target else -1

        return [start, end]
