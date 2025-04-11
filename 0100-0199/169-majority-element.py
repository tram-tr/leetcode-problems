# https://leetcode.com/problems/majority-element

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        res = 0
        for num in nums:
            if count == 0:
                res = num
                count = 1
            else:
                if num == res:
                    count += 1
                else:
                    count -= 1

        return res

