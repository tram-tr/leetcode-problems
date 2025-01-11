# https://leetcode.com/problems/destination-city/

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        sources = set(src for src, _ in paths) # all unique sources
        for src, dst in paths:
            if dst not in sources: # final destination
                return dst
        return None
