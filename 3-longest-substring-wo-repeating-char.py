# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = 0
        end = 0
        window = set()
        max_length = 0

        for end in range(len(s)):
            while s[end] in window:
                window.remove(s[start])
                start += 1
            window.add(s[end])
            max_length = max(max_length, end - start + 1)

        return max_length

