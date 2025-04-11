# https://leetcode.com/problems/reverse-integer

# class Solution:
#     def reverse(self, x: int) -> int:
#         res = 0
#         if x < 0:
#             res = int(str(x)[1:][::-1]) * -1
#         else:
#             res = int(str(x)[::-1])
        
#         if res > 2 ** 31 - 1 or res < -2 ** 31:
#             return 0
        
#         return res

# class Solution:
#     def reverse(self, x: int) -> int:
#         is_negative = False

#         if x < 0:
#             is_negative = True
#             x *= -1
        
#         res = 0
#         while x > 0:
#             res = (res * 10) + (x % 10)
#             x //= 10
        
#         if res > 2 ** 31 - 1:
#             return 0
        
#         return res * -1 if is_negative else res

class Solution:
    def reverse(self, x: int) -> int:
        is_negative = False
        if x < 0:
            is_negative = True
            x *= -1

        res = 0
        while x > 0:
            digit = x % 10
            x //= 10
            if (res > (2 ** 31 - 1) // 10) or (res == (2 ** 31 - 1) // 10 and digit > 7):
                return 0
            res = (res * 10) + digit

        return -res if is_negative else res
                
