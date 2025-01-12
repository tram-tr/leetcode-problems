# https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        counter = Counter(s1)
        left = 0
        count_match = 0

        for right in range(len(s2)):
            if s2[right] in counter and counter[s2[right]] > 0:
                count_match += 1
            counter[s2[right]] -= 1

            while (right - left) + 1 > len(s1):
                if counter[s2[left]] >= 0:
                    count_match -= 1
                counter[s2[left]] += 1
                left += 1

            if count_match == len(s1):
                return True
            
        return False                
