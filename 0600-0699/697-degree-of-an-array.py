# https://leetcode.com/problems/degree-of-an-array/

class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        counter = Counter(nums)
        degree = max(counter.values())

        first = defaultdict(int)
        last = defaultdict(int)
        for i in range(len(nums)):
            if nums[i] not in first:
                first[nums[i]] = i
            last[nums[i]] = i

        res = float('inf')
        for num, cnt in counter.items():
            if cnt == degree:
                res = min(res, last[num] - first[num] + 1)
        
        return res

