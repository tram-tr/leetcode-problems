# https://leetcode.com/problems/substring-with-concatenation-of-all-words/

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        res = []
        counter = Counter(words)
        n = len(words)
        k = len(words[0])

        for i in range(k):
            window = defaultdict(int)
            used = 0
            left = i

            for right in range(left, len(s) - k + 1, k):
                word = s[right:right + k]
                if word not in counter:
                    left = right + k
                    window = defaultdict(int)
                    used = 0
                else:
                    used += 1
                    window[word] += 1
                    while window[word] > counter[word]:
                        window[s[left:left + k]] -= 1
                        left += k
                        used -= 1

                    if used == n:
                        res.append(left)
        
        return res
