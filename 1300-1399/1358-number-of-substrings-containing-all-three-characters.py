# https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/description/

class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0
        window = defaultdict(int)
        left = 0
        
        for right in range(len(s)):
            window[s[right]] += 1

            while len(window) >= 3:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            
            count += left

        return count
