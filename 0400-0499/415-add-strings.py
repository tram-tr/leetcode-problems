# https://leetcode.com/problems/add-strings/description/

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        i = len(num1) - 1
        j = len(num2) - 1
        s = []
        carry = 0

        while i >= 0 and j >= 0:
            d1 = ord(num1[i]) - ord('0')
            d2 = ord(num2[j]) - ord('0')
            sum_d = d1 + d2 + carry

            if sum_d > 9:
                carry = 1
                sum_d = sum_d % 10
            else:
                carry = 0

            s.append(str(sum_d))
            i -= 1
            j -= 1

        while i >= 0:
            d1 = ord(num1[i]) - ord('0')
            sum_d = d1 + carry
            if sum_d > 9:
                carry = 1
                sum_d = sum_d % 10
            else:
                carry = 0
            s.append(str(sum_d))
            i -= 1

        while j >= 0:
            d2 = ord(num2[j]) - ord('0')
            sum_d = d2 + carry
            if sum_d > 9:
                carry = 1
                sum_d = sum_d % 10
            else:
                carry = 0
            s.append(str(sum_d))
            j -= 1

        if carry == 1:
            s.append('1')

        return ''.join(reversed(s))
