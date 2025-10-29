class Solution:
    def smallestNumber(self, n: int) -> int:
        binary=bin(n)[2:]  
        if set(binary)=={'1'}:
            return n
        else:
            flipped=binary.replace('0','1')
            result=int(flipped,2)
            return result
        