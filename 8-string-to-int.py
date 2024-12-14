# https://leetcode.com/problems/string-to-integer-atoi/

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        num = 0
        count = 0
        negative = 1
        for c in s:
            if c == ' ':
                if count == 0:
                    continue
                else:
                    break
            elif c == '-':
                if count == 0:
                    negative = -1
                    count += 1
                else:
                    break
            elif c == '+':
                if count == 0:
                    negative = 1
                    count += 1
                else:
                    break
            elif c in '0123456789':
                num = num * 10 + ord(c) - ord('0')
                count += 1
            else:
                break

        num = num * negative
        if num < -(2**31):
            return -(2**31)
        elif num > (2**31 - 1):
            return (2**31 - 1)
        else:
            return num

            
        