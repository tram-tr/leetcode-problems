# https://leetcode.com/problems/group-anagrams/description/

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        group_count = []
        groups = {}
        for word in strs:
            count = {}
            for c in word:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1

            signature = ""
            for i in range(ord('a'), ord('z') + 1):
                if chr(i) in count:
                    signature += chr(i) + str(count[chr(i)])
                        
            if signature in groups:
                groups[signature].append(word)
            else:
                groups[signature] = [word]

        return list(groups.values())
        