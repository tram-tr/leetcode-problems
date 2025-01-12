# https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/description/

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        window = sum(arr[:k])
        count = 0
        if window >= threshold * k:
            count += 1

        for right in range(k, len(arr)):
            left = right - k
            window += arr[right] - arr[left]
            if window >= threshold * k:
                count += 1
        
        return count
