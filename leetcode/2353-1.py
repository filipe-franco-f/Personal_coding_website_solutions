class FoodRatings:
    
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.foods = foods
        self.cuisines = cuisines
        self.ratings = ratings

    def changeRating(self, food: str, newRating: int) -> None:
        pos = self.foods.index(food)
        self.ratings[pos] = newRating

    def highestRated(self, cuisine: str) -> str:
        highest = 0
        name = None
        for i in range(len(self.foods)):
            if self.ratings[i] > highest and self.cuisines[i] == cuisine:
                highest = self.ratings[i]
                name = self.foods[i]
            elif self.ratings[i] == highest and self.cuisines[i] == cuisine:
                if self.foods[i] < name:
                    name = self.foods[i]
        return name
       

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)