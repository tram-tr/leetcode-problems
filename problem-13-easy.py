class Solution:
    def romanToInt(self, s: str) -> int:
        translate = {
            'I': 1,
            'IV': 4,
            'V': 5,
            'IX': 9,
            'X': 10,
            'XL': 40,
            'L': 50,
            'XC':90,
            'C': 100,
            'CD': 400,
            'D': 500,
            'CM': 900,
            'M': 1000
        }

        # MCMXCIV
        # IV = 4
        # XC = 90
        # CM = 900
        # M = 1000

        # DCXXI
        # I = 1
        # X = 10
        # X = 10
        # C = 100
        # D = 500

        i = len(s) - 1
        ans = 0
        while (i >= 0):
            if (i > 0 and (s[i-1] + s[i]) in translate):
                ans += translate[s[i-1] + s[i]]
                i -= 2
            elif (s[i] in translate):
                ans += translate[s[i]]
                i -= 1
            else:
                break

        return ans
