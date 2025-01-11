# Given an integer array nums and an integer k, return the maximum length of a subarray that sums to k. If there is not one, return 0 instead.


# Example 1:
# Input: nums = [1,-1,5,-2,3], k = 3
# Output: 4
# Explanation: The subarray [1, -1, 5, -2] sums to 3 and is the longest


# Example 2:
# Input: nums = [-2,-1,2,1], k = 1
# Output: 2
# Explanation: The subarray [-1, 2] sums to 1 and is the longest.


# Constraints:
# 1 <= nums.length <= 2 * 105
# -104 <= nums[i] <= 104
# -109 <= k <= 109


#                             j-1  j              i
# ------------------------------------------------------


# 1/ sum[j..i] = k
# 2/ prefix[i] = s
# 3/ prefix[j-1] = s - k


# prefixSum = {
#     key: sum(0..i),
#     value: []
# }


# [1,-1,5,-2,3], k = 3
# i = 4
# s = 6
# s - k = 3
# result = 4


# prefixSum = {
#     1: [0],
#     0: [1], j-1=1 => j = 2 [2..3] = 3
#     5: [2],
#     3: [3], [4..4] = 3
#     6: [4]
# }

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        prefixSum = {}
        s = 0
        n = len(nums)
        res = 0


        for i in range(n):
            s += nums[i]


            if s == k: # 0..i
                res = max(res, i+1)


            if s - k in prefixSum:
                jM1 = prefixSum[s-k]
                j = jM1 + 1
                res = max(res, i - j + 1)


            if s not in prefixSum:
                prefixSum[s] = i


        return res


s = Solution()
print(s.maxSubArrayLen([1,-1,5,-2,3], 3)) # 4
print(s.maxSubArrayLen([-2,-1,2,1], 1)) # 2
