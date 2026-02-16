class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for i in range(32):
            # Get the least significant bit (LSB) of n
            bit = n & 1
            # Shift result left and add the LSB
            result = (result << 1) | bit
            # Shift n right to process the next bit
            n >>= 1
        return result
        