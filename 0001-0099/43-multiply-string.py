# https://leetcode.com/problems/multiply-strings/description/

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        if num1 == '0' or num2 == '0':
            return '0'

        p = [0] * (len(num1) + len(num2))
        for i in range(len(num1) - 1, -1, -1):
            d1 = ord(num1[i]) - ord('0')
            for j in range(len(num2) - 1, -1, -1):
                d2 = ord(num2[j]) - ord('0')
                p[i + j + 1] += (d1 * d2)
                p[i + j] += p[i + j + 1] // 10
                p[i + j + 1] = p[i + j + 1] % 10

        # remove leading 0s
        i = 0
        while i < len(p) and p[i] == 0:
            i += 1 
        p = p[i:]

        return ''.join(map(str, p))

        
