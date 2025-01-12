# https://leetcode.com/problems/count-non-decreasing-subarrays-after-k-operations/

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        cost = 0
        stack = [(nums[-1], 1)] # val, count
        res = 1
        right = len(nums) - 1

        for left in range(len(nums) - 2, -1, -1):
            curr_count = 1
            while stack and stack[-1][0] < nums[left]:
                val, count = stack.pop()
                curr_count += count
                cost += (nums[left] - val) * count

            stack.append((nums[left], curr_count))

            while cost > k:
                val, count = stack.pop(0)
                count -= 1
                cost -= (val - nums[right])
                right -= 1
                if count > 0:
                    stack.insert(0, (val, count))

            res += right - left + 1

        return res
