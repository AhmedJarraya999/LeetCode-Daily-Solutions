class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if 2<n:
            if n%2==0:
                return n
            else:
                return 2*n
        elif n==2 or n==1:
            return n
        