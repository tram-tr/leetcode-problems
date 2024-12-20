# https://leetcode.com/problems/add-binary/

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i = len(a) - 1
        j = len(b) - 1
        s = []
        carry = 0

        while i >= 0 and j >= 0:
            if a[i] != b[j]:
                if carry == 0:
                    s.append('1')
                    carry = 0
                else:
                    s.append('0')
                    carry = 1
            if a[i] == b[j]:
                s.append(str(carry))
                if a[i] == '1':
                    carry = 1
                else:
                    carry = 0
                
            i -= 1
            j -= 1

        while i >= 0:
            if a[i] != str(carry):
                s.append('1')
                carry = 0
            else:
                s.append('0')
                if a[i] == '1':
                    carry = 1
                else:
                    carry = 0
            i -= 1

        while j >= 0:
            if b[j] != str(carry):
                s.append('1')
                carry = 0
            else:
                s.append('0')
                if b[j] == '1':
                    carry = 1
                else:
                    carry = 0
            j -= 1
        
        if carry == 1:
            s.append('1')

        return ''.join(reversed(s))
