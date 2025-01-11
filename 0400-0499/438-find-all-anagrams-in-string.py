# https://github.com/tram-tr/leetcode-problems/new/main

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []

        char_count = Counter(p)
        count = len(char_count)
        start_idx = []

        # sliding window
        left = 0
        right = 0
        while right < len(s):
            c = s[right]

            # decrement the count until 0 
            if c in char_count:
                char_count[c] -= 1
                if char_count[c] == 0:
                    count -= 1
            right += 1

            while count == 0:
                c = s[left]
                # increment the count
                if c in char_count:
                    char_count[c] += 1
                    if char_count[c] > 0:
                        count += 1

                # found anagram
                if right - left == len(p):
                    start_idx.append(left)

                left += 1

        return start_idx

