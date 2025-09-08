class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def has_zero(a):
            return '0' in str(a)
        for a in range(1,n):
            b=n-a
            if not has_zero(b) and not has_zero(a):
                return [a,b]
        