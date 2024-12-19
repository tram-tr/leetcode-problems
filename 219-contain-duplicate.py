# https://leetcode.com/problems/contains-duplicate-ii/description/

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        visited = {}
        for i in range(len(nums)):
            if nums[i] in visited:
                j = visited[nums[i]]
                if abs(i-j) <= k:
                    return True
                
            visited[nums[i]] = i

        return False
