class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) 
        res = r
        
        def canEat(speed):
            hours = 0
            for p in piles:
                hours += (p + speed - 1) // speed
            return hours <= h
        
        while l <= r:
            mid = (l + r) // 2
            if canEat(mid):
                res = mid
                r = mid - 1
            else:
                l = mid + 1
        return res
