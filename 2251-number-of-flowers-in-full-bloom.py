# https://leetcode.com/problems/number-of-flowers-in-full-bloom/description/

from bisect import bisect_left, bisect_right
    
def solution(flowers, people):
    start = [a for a,_ in flowers]
    end = [b for _,b in flowers]
    start.sort()
    end.sort()

    output = []
    for p in people:
        upper = bisect_right(start, p)
        lower = bisect_left(end, p)
        output.append(upper - lower)

    return output

# bisect_left() - return the largest index to insert element with respect <
# bisect_right() - return the largest index to insert element with respect <=

flowers = [[1,6],[3,7],[9,12],[4,13]]
people = [2,3,7,11]
print(solution(flowers, people)) # [1, 2, 2, 2]

flowers = [[1,10],[3,3]]
people = [3,3,2]
print(solution(flowers, people)) # [2,2,1]
