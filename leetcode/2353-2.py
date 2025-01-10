class FoodRatings:
    coises = {}
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        for i in range (len(foods)):
            if not cuisines[i] in self.coises:
                self.coises[cuisines[i]] = {}
            else:
                self.coises[cuisines[i]][foods[i]] = ratings[i]

    def changeRating(self, food: str, newRating: int) -> None:
        for i in range(len(self.coises)):
            if food in self.coises[i]:
                self.coises[i][food] = newRating
                break

    def highestRated(self, cuisine: str) -> str:
        highest = 0
        name = None
        for i in self.coises[cuisine].keys():
            if self.coises[cuisine][i] > highest:
                highest = self.coises[cuisine][i]
                name = i
            elif self.coises[cuisine][i] == highest and i < name:
                highest = self.coises[cuisine][i]
                name = i
        return name

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)