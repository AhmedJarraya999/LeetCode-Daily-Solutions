class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        checker=math.log(n,4)
        return abs(round(checker)- checker)<1e-10

        