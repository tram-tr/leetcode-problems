# https://leetcode.com/problems/design-a-food-rating-system/

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.data = defaultdict(tuple)
        self.heaps = defaultdict(list)

        for f,c, r in zip(foods, cuisines, ratings):
            self.data[f] = (c, r)
            heapq.heappush(self.heaps[c], (-r, f))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, curr_rating = self.data[food]
        self.data[food] = (cuisine, newRating)
        heapq.heappush(self.heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.heaps[cuisine]
        
        while heap:
            rating, food = heap[0]
            if self.data[food][1] != -rating:
                heapq.heappop(heap)
            else:
                return food

        return ''
            
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
