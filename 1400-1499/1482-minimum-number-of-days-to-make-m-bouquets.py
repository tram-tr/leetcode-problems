# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        if m * k > len(bloomDay):
            return -1

        def condition(d):
            count_flower = 0
            count_bouquet = 0
            for i in range(len(bloomDay)):
                if bloomDay[i] <= d:
                    count_flower += 1
                else:
                    count_flower = 0
                if count_flower >= k:
                    count_flower = 0
                    count_bouquet += 1
                    if count_bouquet == m:
                        return True

            return False


        left = 1
        right = max(bloomDay)
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
