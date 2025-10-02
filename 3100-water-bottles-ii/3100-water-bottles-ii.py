#wrong trial

# class Solution:     
#     def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:    
#         empty=0 
#         res=0         
#         while empty<numExchange:             
#             empty+=numBottles           
#             res+=numBottles            
#             if empty>numExchange:                 
#                 numBottles+=1
#                 empty-=numExchange            
#                 res+=1                 
#                 numExchange+=1         
#         return res       



class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        empty=0
        res=0
        res+=numBottles
        empty += numBottles
        while empty>=numExchange:
            empty-=numExchange
            numExchange+=1
            numBottles+=1
            #drink phase
            res+=1
            empty+=1
        return res
        

