# https://leetcode.com/problems/count-the-number-of-good-subarrays/
class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        counter = Counter()
        count = 0
        curr = 0 # current window
        i = 0

        for num in nums:
            curr += counter[num]
            counter[num] += 1
            while curr - counter[nums[i]] + 1 >= k:
                counter[nums[i]] -= 1
                curr -= counter[nums[i]]
                i += 1

            # current window contain at least k pairs
            if curr >= k:
                count += i + 1
        
        return count
