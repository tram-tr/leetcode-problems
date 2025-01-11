# https://leetcode.com/problems/rank-teams-by-votes/description/

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        # initialize an array for 26 possible ranks for each new key
        hmap = defaultdict(lambda: [0] * 26)

        for vote in votes:
            for i in range(len(vote)):
                hmap[vote[i]][i] -= 1 # to sort in reverse order

        # sort by rank (value -> x[1]) then by team name (key -> x[0])
        sorted_rank = sorted(hmap.items(), key=lambda x: (x[1], x[0]))

        # print(sorted_rank)

        return ''.join(team for team, _ in sorted_rank)
