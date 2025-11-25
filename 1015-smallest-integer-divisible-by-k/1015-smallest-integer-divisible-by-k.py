class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        cycle=set()
        remainder=1%k
        l=1
        while remainder!=0:
            remaidner=l%k
            if remainder in cycle:
                return -1
            else:
                cycle.add(remainder)
                remainder = (remainder * 10 + 1) % k
                l+=1
        return l

            


        