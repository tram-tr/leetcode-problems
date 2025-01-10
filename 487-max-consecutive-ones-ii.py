# https://leetcode.com/problems/max-consecutive-ones-ii/description/

'''
Given a binary array nums, return the maximum number of consecutive 1's in the array if you can flip at most one 0.

Example 1:
Input: nums = [1,0,1,1,0]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1] and we have 3 consecutive ones.
The max number of consecutive ones is 4.


Example 2:
Input: nums = [1,0,1,1,0,1]
Output: 4
Explanation:
- If we flip the first zero, nums becomes [1,1,1,1,0,1] and we have 4 consecutive ones.
- If we flip the second zero, nums becomes [1,0,1,1,1,1] and we have 4 consecutive ones.
The max number of consecutive ones is 4.


Constraints:
1 <= nums.length <= 10^5
nums[i] is either 0 or 1.
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        left, right = 0, 0
        length = 0
        for right in range(len(nums)):


            while counter > 1: # counter == 1 and nums[right] == 0
                if nums[left] == 0:
                    counter -= 1
                left += 1
            if nums[right] == 0:
                counter += 1
            length = max(length, right - left + 1)


        return length


s = Solution()
print(s.findMaxConsecutiveOnes([1,0,1,1,0])) # 4
print(s.findMaxConsecutiveOnes([1,0,1,1,0,1])) # 4
