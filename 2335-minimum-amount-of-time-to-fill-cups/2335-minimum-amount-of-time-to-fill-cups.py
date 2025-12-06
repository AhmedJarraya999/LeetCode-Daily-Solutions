class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a,b,c=amount
        return max(max(a, b, c), (a + b + c + 1) // 2)





        