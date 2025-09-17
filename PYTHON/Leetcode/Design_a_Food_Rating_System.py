class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.tracker = {}
        self.ratings = defaultdict(list)
        for f, c, r in zip(foods, cuisines, ratings): 
            self.tracker[f] = (c, r)
            heapq.heappush(self.ratings[c],[-r, f])

    def changeRating(self, food: str, newRating: int) -> None:
        c, r = self.tracker[food]
        heapq.heappush(self.ratings[c],[-newRating, food])
        # Update teh tracker
        self.tracker[food] = c, newRating
    

    def highestRated(self, cuisine: str) -> str:
        # remove all the redundant entries
        heap = self.ratings[cuisine]
        # now remove all the redundant
        while self.tracker[heap[0][1]][1] != -heap[0][0]:
            heapq.heappop(heap)

        return heap[0][1]
