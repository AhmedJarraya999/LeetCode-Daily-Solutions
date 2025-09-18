from sortedcontainers import SortedSet  


class FoodRatings:

    def __init__(self, foods, cuisines, ratings):
        self.cuisine_food=defaultdict(SortedSet)#cuisine->(rating,food)
        self.cuisines={} #food->cuisine
        self.ratings={}#food->rating
        for i in range(len(foods)):
            self.cuisine_food[cuisines[i]].add((-ratings[i],foods[i]))
            self.cuisines[foods[i]]=cuisines[i]
            self.ratings[foods[i]]=ratings[i]
        

    def changeRating(self, food, newRating):
        c=self.cuisines[food]
        r=self.ratings[food]
        self.cuisine_food[c].remove((-r,food))
        self.cuisine_food[c].add((-newRating, food))
        self.ratings[food]=newRating
     

    def highestRated(self, cuisine):
         return self.cuisine_food[cuisine][0][1]


# from sortedcontainers import SortedDict


# class FoodRatings:

#     def __init__(self, foods, cuisines, ratings):
#         self.food_to_cuisine = {}
#         self.food_to_rating = {}
#         self.cuisine_to_foods = {}

#         for food, cuisine, rating in zip(foods, cuisines, ratings):
#             self.food_to_cuisine[food] = cuisine
#             self.food_to_rating[food] = rating

#             if cuisine not in self.cuisine_to_foods:
#                 self.cuisine_to_foods[cuisine] = SortedDict()

#             # Using negative rating to sort descending
#             if -rating not in self.cuisine_to_foods[cuisine]:
#                 self.cuisine_to_foods[cuisine][-rating] = set()
#             self.cuisine_to_foods[cuisine][-rating].add(food)

#     def changeRating(self, food, newRating):
#         oldRating = self.food_to_rating[food]
#         cuisine = self.food_to_cuisine[food]

#         # Remove from old rating
#         self.cuisine_to_foods[cuisine][-oldRating].remove(food)
#         if not self.cuisine_to_foods[cuisine][-oldRating]:
#             del self.cuisine_to_foods[cuisine][-oldRating]

#         # Add to new rating
#         if -newRating not in self.cuisine_to_foods[cuisine]:
#             self.cuisine_to_foods[cuisine][-newRating] = set()
#         self.cuisine_to_foods[cuisine][-newRating].add(food)

#         self.food_to_rating[food] = newRating

#     def highestRated(self, cuisine):
#         # Get the highest rating (smallest negative)
#         highest_rating = next(iter(self.cuisine_to_foods[cuisine]))
#         return min(self.cuisine_to_foods[cuisine][highest_rating])
