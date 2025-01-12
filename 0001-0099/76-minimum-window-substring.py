# https://leetcode.com/problems/minimum-window-substring/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        
        counter = Counter(t)
        left = 0
        res = 0
        count_match = 0
        length = float('inf')
        for right in range(len(s)):
            if s[right] in counter and counter[s[right]] > 0:
                count_match += 1
            counter[s[right]] -= 1

            while count_match == len(t):
                if right - left + 1 < length:
                    res = left
                    length = right - left + 1
                
                counter[s[left]] += 1
                if counter[s[left]] > 0:
                    count_match -= 1
                left += 1
            

        if length == float('inf'):
            return ""
        
        return s[res:res + length]
