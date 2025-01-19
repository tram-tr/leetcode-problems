# https://leetcode.com/problems/ugly-number-iii/

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:

        def lcm(x, y):
            return x * y // math.gcd(x, y)

        def condition(x):
            return (x // a + x // b + x // c 
                    - x // lcm(a, b) - x // lcm(b, c) - x // lcm(a, c)
                    + x // lcm(lcm(a, b), c)) >= n

        left = min(a, b, c)
        right = 2 * 10 ** 9
        
        while left < right:
            mid = left + (right - left) // 2
            if condition(mid):
                right = mid
            else:
                left = mid + 1

        return left
