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
        