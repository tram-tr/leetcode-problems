# https://leetcode.com/problems/median-of-two-sorted-arrays/

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)

        m = len(nums1)
        n = len(nums2)
        left = 0
        right = m

        while left < right:
            mid1 = left + (right - left) // 2
            mid2 = (m + n + 1) // 2 - mid1

            l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = nums1[mid1] if mid1 < m else float('inf')
            l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = nums2[mid2] if mid2 < n else float('inf')

            if l1 > r2 or l2 <= r1:
                right = mid1
            else:
                left = mid1 + 1 

        # found the part, calculate the median
        mid1 = left
        mid2 = (m + n + 1) // 2 - mid1

        l1 = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
        r1 = nums1[mid1] if mid1 < m else float('inf')
        l2 = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
        r2 = nums2[mid2] if mid2 < n else float('inf')

        if l1 <= r2 and l2 <= r1:
            if (m + n) % 2 == 0:
                return (max(l1, l2) + min(r1, r2)) / 2.0
            else:
                return max(l1, l2)

        return 0.0
