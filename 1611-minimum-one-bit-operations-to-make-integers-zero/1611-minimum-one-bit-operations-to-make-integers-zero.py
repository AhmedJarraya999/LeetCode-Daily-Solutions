class Solution:
    def minimumOneBitOperations(self, n: int) -> int:
        if n == 0:
            return 0
        
        msb = n.bit_length() - 1
        return (1 << (msb + 1)) - 1 - self.minimumOneBitOperations(n ^ (1 << msb))
