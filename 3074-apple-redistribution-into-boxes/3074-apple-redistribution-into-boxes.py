class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse=True)
        total_apples =sum(apple)
        res=0
        cur=0
        for cap in capacity:
            cur+=cap
            res+=1
            if cur>=total_apples:
                return res



                



        