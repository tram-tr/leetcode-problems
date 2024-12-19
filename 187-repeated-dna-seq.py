# https://leetcode.com/problems/repeated-dna-sequences/description/

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hmap = {}
        sequences = []
        for i in range(len(s) - 9):
            seq = s[i:i+10]
            if seq in hmap and seq not in sequences:
                sequences.append(seq)
            hmap[seq] = hmap.get(seq, 0) + 1

        return sequences
