# https://leetcode.com/problems/k-th-smallest-prime-fraction/description/

class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:
        n = len(arr)

        def condition(x):
            count = 0
            num = arr[0]
            dem = arr[n - 1]
            j = 0
            
            for i in range(1, n):
                while arr[j] <= arr[i] * x:
                    j += 1
                
                count += j
                if j > 0 and arr[j - 1] * dem > arr[i] * num:
                    num = arr[j - 1]
                    dem = arr[i]
            
            return count, num, dem

        left = 0
        right = 1.0

        while right - left > 1e-9:
            mid = left + (right - left) / 2
            count, num, dem = condition(mid)
            
            if count == k:
                return [num, dem]
            elif count > k:
                right = mid
            else:
                left = mid

        return []



