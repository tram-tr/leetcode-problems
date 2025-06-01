# https://leetcode.com/problems/check-if-array-is-good/

class Solution:
    def isGood(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False

        counter = Counter(nums)

        n = len(nums)-1
        if n not in counter or counter[n] != 2:
            return False

        for num in range(1, n):
            if num not in counter or counter[num] != 1:
                return False

        for num in counter:
            if num < 1 or num > n:
                return False

        return True
