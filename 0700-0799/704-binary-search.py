# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            # 1 2 3 4
            # 1 2 2 2 2 2 3
            mid = left + (right - left) // 2
            # mid = right - (right - left) // 2
            # if nums[mid] == target:
            #     return mid
            if nums[mid] >= target:
                right = mid
            else:
                left = mid + 1

        return left if nums[left] == target else -1
