from sortedcontainers import SortedDict

class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.food_to_cuisine = {}
        self.food_to_rating = {}
        self.cuisine_to_foods = {}
        
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_to_cuisine[food] = cuisine
            self.food_to_rating[food] = rating
            
            if cuisine not in self.cuisine_to_foods:
                self.cuisine_to_foods[cuisine] = SortedDict()
            
            # Using negative rating to sort descending
            if -rating not in self.cuisine_to_foods[cuisine]:
                self.cuisine_to_foods[cuisine][-rating] = set()
            self.cuisine_to_foods[cuisine][-rating].add(food)

    def changeRating(self, food, newRating):
        oldRating = self.food_to_rating[food]
        cuisine = self.food_to_cuisine[food]
        
        # Remove from old rating
        self.cuisine_to_foods[cuisine][-oldRating].remove(food)
        if not self.cuisine_to_foods[cuisine][-oldRating]:
            del self.cuisine_to_foods[cuisine][-oldRating]
        
        # Add to new rating
        if -newRating not in self.cuisine_to_foods[cuisine]:
            self.cuisine_to_foods[cuisine][-newRating] = set()
        self.cuisine_to_foods[cuisine][-newRating].add(food)
        
        self.food_to_rating[food] = newRating

    def highestRated(self, cuisine):
        # Get the highest rating (smallest negative)
        highest_rating = next(iter(self.cuisine_to_foods[cuisine]))
        return min(self.cuisine_to_foods[cuisine][highest_rating])
