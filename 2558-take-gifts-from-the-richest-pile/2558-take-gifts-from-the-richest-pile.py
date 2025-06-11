class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for _ in range(k):
            gifts.sort()
            #reduce largest one
            gifts[-1]=isqrt(gifts[-1])
        res=sum(gifts)
        return res



        