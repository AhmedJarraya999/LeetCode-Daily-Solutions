class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n<=0:
            return False
        checker=math.log(n,3)
        return abs(round(checker)-checker)<1e-10
        