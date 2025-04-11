# https://leetcode.com/problems/valid-triangle-number

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        def lower_bound(arr, target, l):
            r = len(arr)
            while l < r:
                m = l + (r - l) // 2
                if arr[m] < target:
                    l = m + 1
                else:
                    r = m
            return l

        nums.sort()
        res = 0
        n = len(nums)
        for i in range(n - 2):
            if nums[i] == 0:
                continue


            for j in range(i + 1, n - 1):
                target = nums[i] + nums[j]
                k = lower_bound(nums, target, j + 1)
                # all indices from j+1 to k-1 satisfy the triangle condition nums[i] + nums[j] > nums[k]
                res += k - j - 1

        return res
