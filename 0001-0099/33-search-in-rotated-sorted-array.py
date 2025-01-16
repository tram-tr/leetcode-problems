# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            if nums[mid] <= nums[right]:
                right = mid
            else:
                left = mid + 1

        if target == nums[left]:
            return left
        else:
            l = left
            r = len(nums) - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1
            
            if nums[l] == target:
                return l

            l = 0
            r = left - 1
            while l < r:
                m = l + (r - l) // 2
                if nums[m] >= target:
                    r = m
                else:
                    l = m + 1

            return l if nums[l] == target else -1
