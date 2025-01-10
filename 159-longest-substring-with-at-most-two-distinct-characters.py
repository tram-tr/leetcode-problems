# https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters

'''
Given a string s, return the length of the longest
substring
 that contains at most two distinct characters.




Example 1:
Input: s = "eceba"
Output: 3
Explanation: The substring is "ece" which its length is 3.
Example 2:




Input: s = "ccaabbb"
Output: 5
Explanation: The substring is "aabbb" which its length is 5.


Constraints:
1 <= s.length <= 105
s consists of English letters.
'''

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        window = defaultdict(int)
        left = 0
        res = 0


        for right in range(len(s)):
            window[s[right]] += 1
            while len(window) > 2:
                window[s[left]] -= 1
                if window[s[left]] == 0:
                    del window[s[left]]
                left += 1
            res = max(res, right - left + 1)


        return res

s = Solution()
print(s.lengthOfLongestSubstringTwoDistinct("eceba")) # ouput 3
print(s.lengthOfLongestSubstringTwoDistinct("ccaabbb")) # output 5
