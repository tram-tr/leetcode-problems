# https://leetcode.com/problems/continuous-subarray-sum/
#                                   j-1  j         i
# ----------------------------------------------------------


# 1/ arr[j..i] % k == 0
# 2/ prefix[i] = s % k = d
# 3/ prefix[j-1] % k = d


# a % k = x
# b % k = y
# (a-b) % k = (x-y) % k


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefixSum = {}
        s = 0
        n = len(nums)
        res = 0


        for i in range(n):
            s += nums[i]


            if s % k == 0: # 0..i
                res = max(res, i+1)


            if s % k in prefixSum:
                jM1 = prefixSum[s % k]
                j = jM1 + 1
                res = max(res, i - j + 1)


            if s % k not in prefixSum:
                prefixSum[s % k] = i


        return res > 1


s = Solution()
print(s.checkSubarraySum([23,2,4,6,7], 6)) # true
print(s.checkSubarraySum([23,2,6,4,7], 6)) # true
print(s.checkSubarraySum([23,2,6,4,7], 13)) # false
print(s.checkSubarraySum([2,1,5], 6)) # true
print(s.checkSubarraySum([5,0,0,0], 3)) # true
print(s.checkSubarraySum([2,4,3], 6)) # true
