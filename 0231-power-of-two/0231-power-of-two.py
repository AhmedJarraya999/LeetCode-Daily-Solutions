class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n>0 and math.log2(n).is_integer()
        